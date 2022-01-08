# copy and paste your server.py code from the labs
# don't modify this imports.
import socket
from threading import Thread
from client_handler import ClientHandler
import asyncio



class Server(object):
    """
    The server class implements a server socket that can handle multiple client connections.
    It is really important to handle any exceptions that may occur because other clients
    are using the server too, and they may be unaware of the exceptions occurring. So, the
    server must not be stopped when a exception occurs. A proper message needs to be show in the
    server console.
    """
    MAX_NUM_CONN = 10  # keeps 10 clients in queue

    def __init__(self, host="127.0.0.1", port=12000):
      
        self.host = host
        self.port = port

        # your implementation for this socket here
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handlers = {}  # initializes client_handlers list

    def _bind(self):
      
        #Binding the server socket to the Host and Port
        self.server.bind((self.host,self.port))
        

    def _listen(self):
    

        #Listening
        self.server.listen(self.MAX_NUM_CONN)
        print(f'Listening at {self.host}/{self.port}')
   

    def _accept_clients(self):
      
        print("In the Accepting")

        while True:

            #Accepting the connection with the client
            clienthandler, addr = self.server.accept()
            
            #Creating the thread
            Thread(target=self._handler, args = (clienthandler,addr)).start()

            

            
            print("Thread Made")

    def _handler(self, clientsocket, addr):
   
       
        #Creating the ClientHandler obj
        obj = ClientHandler(self, clientsocket, addr)

        #Adding the handler object to the dictionary of handlers
        self.handlers[addr[1]]  = obj

        obj.run()   
        
      

    def run(self):
      
        self._bind()
        self._listen()
        self._accept_clients()


# main execution
if __name__ == '__main__':
    server = Server()
    server.run()
