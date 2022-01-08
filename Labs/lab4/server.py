# don't modify this imports.
import socket
from threading import Thread
from clienthandler import ClientHandler



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
        """
        TODO: copy and paste your implementation from lab 3 for self.server socket property
        """
        self.host = host
        self.port = port

        # your implementation for this socket here
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handlers = {}  # initializes client_handlers list

    def _bind(self):
        """
        TODO: copy and paste your implementation from lab 3
        :return: VOID
        """
        #Binding the server socket to the Host and Port
        self.server.bind((self.host,self.port))
        

    def _listen(self):
        """
        TODO: copy and paste your implementation from lab 3
        :return: VOID
        """


        #Listening
        if self.server:

            self.server.listen(self.MAX_NUM_CONN)
            
            print("Server is running with out issues")
            
            print(f'Listening at {self.host}/{self.port}')    
        
        else:
            
            print("Server has failed to Listen and is Not Running")
        
   

    def _accept_clients(self):
        """
        #TODO: Modify your implementation from lab 3, so now the
               server can support multiple clients pipelined.
               HINT: you must thread the handler(...) method
        :return: VOID
        """
        print("In the Accepting")

        while True:

            #Accepting the connection with the client
            clienthandler, addr = self.server.accept()
            
            #Creating the thread
            Thread(target=self._handler, args = (clienthandler,addr)).start()
            

    def _handler(self, clientsocket, addr):
        """
        TODO: create an object of the ClientHandler.
              see the clienthandler.py file to see
              the parameters that must be passed into
              the ClientHandler's constructor to create
              the object.
              Once the ClientHandler object is created,
              add it to the dictionary of client handlers initialized
              on the Server constructor (self.handlers)
        :clienthandler: the clienthandler child process that the server creates when a client is accepted
        :addr: the addr list of server parameters created by the server when a client is accepted.
        """
   
        #Creating the ClientHandler obj
        obj = ClientHandler(self, clientsocket, addr)

        #Adding the handler object to the dictionary of handlers
        #self.handlers[addr[1]]  = obj
        self.handlers.append(obj)

        obj.run()
      

    def run(self):
        """
        Already implemented for you
        Run the server.
        :return: VOID
        """
        self._bind()
        self._listen()
        self._accept_clients()


# main execution
if __name__ == '__main__':
    server = Server()
    server.run()
