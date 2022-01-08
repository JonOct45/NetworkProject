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

import pickle
import threading
import queue




from menu import Menu
# from protocol.udp_socket import UDPSocket
from threading import Thread
# from protocol.CDMA_Protocol import CDMA_Protocol
from PGP import PGP_protocol as PGP
import math
from LinkState import LinkState as LS
from CDMA_Protocol import CDMA_Protocol as CDMA
from collections import defaultdict


class ClientHandler:

    def __init__(self, server_instance, clienthandler, addr):
            self.server_ip = addr[0]
            self.client_id = addr[1]
            self.server = server_instance
            self.handler = clienthandler
            self.print_lock = threading.Lock()
            self.username = ""
            self.close = False

            self.network_map = None
            self.matrix_map = []
            self.clients = []

            '''
            Storing the codes for clients, '''
            self.chatHeader = "CHAT"
            self.list_of_clients = []
            self.keys = {}
            self.channels = {}
            self.channel_id = 0
           
            """CDMA Attributes"""
            if not hasattr(self.server, 'cdma'):
                self.server.cdma = CDMA()
                self.server.cdma.generate_codes(10, 10)
            code_idx = len(self.server.handlers)
            self.code = self.server.cdma.code_set[code_idx-1]
    
            self.messages = defaultdict(list)

           
           
            """"
            if client_id not in self.messages.keys():
                self.messages[client_id] = [message]
            else: self.messages[client_id].append(message)
            
            """
    
    def generate_matrix(self):  
        print("Generating Matrix")

        users_length = len(self.server.handlers.keys())

        map_matrix = LS.random_matrix(users_length)

        print("Generated Matrix")
        
        self.client_list = []
        for keys in self.server.handlers.keys():

            
            self.server.handlers[keys].matrix_map = map_matrix
            self.client_list.append(self.server.handlers[keys].username)

        network_map = LS.create_network(self.client_list, map_matrix)
        print("Created Network")

        for keys in self.server.handlers.keys():

            self.server.handlers[keys].network_map = network_map

        print(f"The Network Map is:\n {network_map}")

    def process_data(self):

        request = self.receive()

        print(f'Received request: {request}')

        data = request['option']
        data = str(data)
        if data == '1':
            self.process_1(request)

        elif data == '2':
            self.process_2(request)

        elif data == '3':
            self.process_3(request)

        elif data == '4':
            self.process_4(request)

        elif data == '5':  
            self.process_5(request)

        # elif data == '6':
        #     self.process_6(request)

        # elif data == '7':
        #     self.process_7(request)
        
        # elif data == '8':
        #     self.process_8(request)
        elif data == '9':
            self.process_9(request)

        # elif data == '10':
        #     self.process_10(request)
        
        # elif data == '11':
        #     self.process_11(request)
        
        elif data == '13':
            self.process_13(request)

        else:
            response = Menu.response_headers()[0]
            response["body"] = "Not implimented yet"
            self.send(response)

    def process_1(self, request):
        #Need to get the client list from the server, displaying the ID and Name        
        user_list = "List of Users:\n"
       
        for user in self.server.handlers.keys(): 
            name = self.server.handlers[user].username
            client = self.server.handlers[user].client_id

            print("Printing from List")
            user_list += f'{name} : {client}\n'

          
        response = Menu.response_headers()[0] # todo get actual headers
        response['body'] = user_list 
        print(f'Sending: {response}')
        self.send(response)

        # self.send("{}\nYour option <enter a number>: ".format(user_list))

    def process_2(self, request):
        '''
        TODO
        We have to get the name of the sender, the message and the reciever. The receiver
        will be a client object in the Servers handlers dict that is created on the Server.py 
        
        Will be using a Try Except to attempt setting the data in the server, will need to consider
        the race conditions, 
        
        Code has some errors when I try to retrieve data from the server, will cause client to crash sometimes.
        
        '''
        # #Receiving the sender name
        # self.send("Who is the sender?")
        # sender = self.receive()

        # #Receiving the message
        # self.send("What is the message?")
        # message = self.receive()

        # #Recieving the receiver client ID
        # self.send("What is the receiver?")
        # receiver = self.receive()
        # print(receiver)
        
        sender = self.client_id
        message = request['message']
        receiver = request['recipient']

        tuples = ("d", message)
        response = Menu.response_headers()[1]

        try:          
            #Setting the message received into the dictionary of handlers on the server.py
            self.server.handlers[int(receiver)].messages[sender].append(tuples)            
            print(self.server.handlers[int(receiver)].messages)
            response['body'] = 'Message sent!'
            self.send(response)
        except:
            response['body'] = 'Message not sent.'
            self.send(response)
    
    def process_3(self, reqeust):
        #print(list(self.server.handlers[self.client_id]))
        print("In Process 3")
        all_messages = ''
        message_list = []

        for sender in self.messages:
            message_list.extend(self.messages[sender])

            # message_line = f' : {self.messages[sender]}, {sender} sent as personal message\n'
            # all_messages += message_line
        
        response = Menu.response_headers()[2]
        response['messages'] = message_list
             
        self.send(response)
        
        # print("Attempting to clear messages")
        self.messages.clear()
        print("Cleared Messages")

    def process_4(self, request):
        # firstthread = Thread(target=self.udp_socket.receivem)
        # firstthread.start()   
        '''
        TODO
        We need to take information in from the client about the UDP we wish to connect to. 
        Also will need to access the correct client to send to. 
        Verifying -> Binding -> Sending -> -> Let Client Know
        '''
        #Binding to the correct client
        # self.send("Enter the address to bind your UDP client (e.g 127.0.0.1:6000): ")
        # self.bind = self.receive()
        # self.bind = self.bind.split(":")

        #Test Data for UDP
        # self.testserverip = '127.0.0.1'

        #Setting the Binding Tuple
        # self.bind_tuple = (self.bind[0], int(self.bind[1]))
        
        response = Menu.response_headers()[3]
        send_address = request['send_address']
        receive_address = request['receive_address']
        send_ip, send_port = send_address.split(':')
        receive_ip, receive_port = receive_address.split(':')

        response['send_ip'] = send_ip
        response['send_port'] = send_port
        response['receive_ip'] = receive_ip
        response['receive_port'] = receive_port
        response['message'] = request['message']
        self.send(response)
  
    def process_5(self, request):

   

        received_message = request['message']

        #Encoding the message
        message = self.server.cdma.encode_all(received_message)
        print(f"The Encodes Message is: {message}")

        #Creating the Broadcast Tuple
        broadcast_tuple = ("b", message)
        for client in self.server.handlers.keys():
            self.server.handlers[client].messages[self.client_id].append(broadcast_tuple)
    
        # self.print_lock.release()

        response = Menu.response_headers()[4] 
        response['body'] = f'Broadcasted message: \"{message}\"'

        self.send(response)      
        
        
        # self.send("Data is {}".format(message))


        #Will need to Encode and send to all of the clients on the server.

    def process_6(self, requeset):
   
        # self.send("Enter the new channel id:")
        # self.channel_id = self.receive()

        # #Creating the channel


        # print("Making Data")
        # data = PGP()
        # print("Data Made")

        # n,e,d = data.RSA_encrypt()
        # print(f"N Value: {n}, E Value: {e}, D Value: {d}")

        # encrcpted = data.PublicKeys(n,e,)
        
      
        # self.send(f'You\'ve Chosen Option 6. Testing')
        pass

    def process_7(self, request):
        #Creating a secure channel to chat with other users.
        self.send("Enter the channel id you'd like to join: ")
        # self.channel_id[] = self.receive()


        self.server.handlers[self.client_id].keys["Topics"] = ["What?", "Why?", "How?"]
        print(self.server.handlers[self.client_id].keys)
        self.send("You've Chosen Option 7.")

    def process_8(self, request):
        #Creating a secure channel to chat with other users.
        term = self.server.handlers[self.client_id].keys["Topics"][0]
        self.send(term)
        #self.send("You've Chosen Option 8.")

    def process_9(self, request):
        #Generating a random matrix map for the number of users on the server.
        if len(self.server.handlers.keys()) != len(self.matrix_map):
            self.generate_matrix()

        print(self.matrix_map)
        response = Menu.response_headers()[8]
        response['body'] = self.network_map

        self.send(response)
        # print("Started Thread")

    def process_10(self, request):
        print('Starting process 10')
        src = self.client_list.index(self.username)

        print(f'Calculating with: {self.matrix_map}\t{src}')
        distance_matrix = LS.dijkstras(self.matrix_map, src) 
        print(f'distance matrix: {distance_matrix}')
        response = Menu.response_headers()[9]
       
        response['body'] = distance_matrix

        print(f'sending: {response}')
        
        self.send(response)
        

    def process_11(self, request):


    
        self.names_list = [self.server.handlers[users].username for users in self.server.handlers.keys()]
        count = len(self.server.handlers.keys())

        Liked = LS()


        Matrix2 = Liked.random_matrix(count)

        MatrixLength = len(Matrix2)
        # LikedAnswered = Thread(target=Liked.random_matrix, args = (count,)).start()

        # Liked.join()

        self.send(f"The Matrix is:\n {Matrix2}\n And the length is: {MatrixLength}")

    def process_13(self, request):
        #Will disconnect the client from the server.
        response = Menu.response_headers()[12]
        self.send(response)

        # self.client_handler.close()
        
        del self.server.handlers[self.client_id]
        self.handler.close()
        self.close = True
    
    def send(self, message):
        print("Sent")
        self.handler.send(pickle.dumps(message))
        return True

    def receive(self, max_alloc_buffer=40000):
        self.pickle_data = self.handler.recv(max_alloc_buffer)
        self.data = pickle.loads(self.pickle_data)
        return self.data
    
    def sendID(self, clientid):
        data = {'clientid': clientid}
        self.send(data)

    def update_client_list(self, clientid):
        self.server.list_of_clients.append(clientid)

    def run(self):
        headers = (Menu.get(), Menu.request_headers())        
        self.send(["Enter your Username: ",self.code, headers])
        self.username = self.receive()
        self.send(f"Your client info is:\nClient Name: {self.username}\nClient ID: {self.client_id}\n")
        
        while not self.close:
            try:
                
                self.process_data()
                

            except:
                self.handler.close()
                break  

