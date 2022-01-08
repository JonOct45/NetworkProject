########################################################################################################################
# Class: Computer Networks
# Date: 10/18/2021
# Project: TCP/UDP Centralized Client-Server Network
# Goal: Learning Networking in Python with TCP sockets
# Student Name: Jonathan McGrath
# Student ID: 918145233
# Student Github Username: JonOct 45
# Lab Instructions: No partial credit will be given. Labs must be completed in class, and must be committed to your
#               personal repository by 9:45 pm.
# Running instructions: This program needs the server to run. The server creates an object of this class.
#
########################################################################################################################
from threading import Thread 
import socket 
import pickle
from CDMA_Protocol import CDMA_Protocol as CDMA

# from protocol.udp_socket import udp_socket
# from protocol.PGP import PGP

class ClientHelper:
    START_UDP = 112109
    
    def __init__(self, client):
        self.client = client
        self.exit = False
        self.cdma = CDMA()
        self.CDMACodes = None
        self.handshake()
        self.udp_socket = None
        """Private Key will be on the client"""

    def handshake(self):
        data = self.client.receive()     
        self.CDMACodes = data[1]
        menu = data[2]
        self.text_menu = menu[0]
        self.request_headers = menu[1]
        self.username = input(data[0])
        self.send_username()
        print(self.client.receive())

    def send_username(self):
        self.client.send(self.username)

    # Need to send a request to the server
    def send_request(self,option):

        request_header = self.request_headers[option-1]
        
        for prompt, key in request_header['prompts']:
            data = input(prompt)
            request_header[key] = data 
            
        self.client.send(request_header)

    #Need to process a response from the server
    def process_response(self):
        response = self.client.receive()
        
        print(f'Received response: {response}')
        header = response['header']

        if header == 'text':
            print(response['body'])
        elif header == 'messages':
            self.process_messages(response['messages'])
        elif header == 'UDP':
            # TODO: openUDP socket and send
            message = response['message']
            send_ip = response['send_ip']
            send_port = response['send_port']
            self.ip = response['receive_ip']
            self.port = response['receive_port']

            self.send_udp(message, send_ip, send_port) # todo implement
        elif header == 'channel':
            self.join_channel( ) # TODO: implement join channel
        elif header == 'exit':
            self.exit = True
        else:
            print("bad response header")
    
    # decode received messages on client side
    def process_messages(self, messages):
        for flag, message in messages:
            if flag == 'b': # broadcasted messages
                # decode
                message = self.cdma.decode(message, self.CDMACodes)
                print(message)
            elif flag == 'd': # direct messages
                print(message)
            else:
                print('Could not decode message')

    def join_channel():
        pass

    def send_udp(self, message, recipient_ip, recipient_port):
        self.open_udp(self.ip, self.port)
        self.udp_socket.sendto(pickle.dumps(message), (recipient_ip, int(recipient_port)))

    def open_udp(self, ip, port):
        if self.udp_socket is None:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind((ip, int(port)))
            Thread(target=self.udp_listen).start()
            print(f'Opened UDP socket at {self.ip}:{self.port}')
        else:
            print('UDP socket already runnning')

    def udp_listen(self, max_alloc_buffer=4090):
        while True: 
            try:
                data, addr = self.udp_socket.recvfrom(max_alloc_buffer)
                deserial_data = pickle.loads(data)
                print(f'UDP GRAM RECEIVED FROM {addr}: {deserial_data}')
            except:
                print('Connection does not exist')
    # Start the client helper
    def start(self):
        while True:
            print(self.text_menu + '\n')

            option = input("Enter your option: ")
             
            self.send_request(int(option))
            self.process_response()
            
            if self.exit:
                break

        self.client.close()
        print('Client closed. Goodbye!')

    '''
    OPTION 4 UDP METHODS

    Here is where we will implament the Sockets and Encoding for the client
    UDP Methods
    
    '''

    '''
    OPTION 5 CDMA METHODS
    Here is where we will put CDMA Encoding / Decoding

    Will need to store codes for users either here or on the server

    '''

    '''
    OPTION 6 PGP METHODS
    Here we will put PGP Methods creating a secure channel to chat with clients
    
    Will need Channel ID sent to the server as a Request 
    
    Client will create the ID and send to the server
    Clients will check the server for the ID
    '''
    
