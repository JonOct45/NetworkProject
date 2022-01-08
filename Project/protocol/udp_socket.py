# UDP socket

import socket


class UDPSocket:

    def __init__(self, port):
        self.port = port
        self.ipv4 = socket.AF_INET
        self.transmission_protocol = socket.SOCK_DGRAM
        self.udp_socket = socket.socket(self.ipv4, self.transmission_protocol)
        self.listen()

    def listen(self):
        try:
            self.bind()
            print(f'UDP socket successfully bind to port {self.port}')
        except ConnectionError as err:
            print("An error occurred: ", err.args[1])

    def bind(self):
        print("Binding...")
        address = ('', self.port)
        print(address)
        self.udp_socket.bind(address)
        print("Binding successful")


    def send(self, message, to=None, broadcast=False, toItself=False):
        print("Attempting to Send TO {}".format(to))
        
        if broadcast:
            self.broadcast(message, toItself)
        else:
            self.udp_socket.sendto(message, to)


    def broadcast(self, message, toItself=False):
        print("Broadcasting...")
        socket_option = socket.SOL_SOCKET
        transmission_method = socket.SO_BROADCAST
        active = 1
        self.udp_socket.setsockopt(socket_option, transmission_method, active)
        address = ('<broadcast>', self.port)
        print("Set up: {}".format(message))
        print("This is Address: {}".format(address))
        self.udp_socket.sendto(message, address)
        if toItself:
            self.print_response(is_broadcast=True)

    '''
    Testing Sending / Receiving 
    '''
    #Testing Function
    # def receivem(self, mem_alloc=4096):
    #     print("Waiting for response... M")
    #     while True:
    #         data, addr = self.udp_socket.recvfrom(mem_alloc) 
    #         print("True Response, Data : {}, ADDR: {}".format(data, addr))
    #         print(f'{data} from {addr}')
    #         break
        
    #     print("Response Received M")

    # def send(self, message, to): 

    #     print("Attempting to send TO {}".format(to))

    #     self.udp_socket.sendto(message, to)

    #     print("Send TO")

    '''
    Ending of Send / Recieve Methods
    '''

    def print_response(self, is_broadcast=False, mem_alloc=4096):
        print("Waiting for response...")
        while True:
           
            data, addr = self.udp_socket.recvfrom(mem_alloc) 
            print("True Response, Data : {}, ADDR: {}".format(data, addr))
            if is_broadcast:
                print(f'Message broadcast: {data}  from {addr}')
                break
            else:
                print(f'{data} from {addr}')
                break
        
        print("Response received")


# udp_socket = UDPSocket(12006)
# message = b'this is my message'  # need to abe in bytes

# udp_socket.send(message,to = ('192.168.1.10', 12006), broadcast=True, toItself=True)


