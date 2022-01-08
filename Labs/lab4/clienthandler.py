########################################################################################################################
# Class: Computer Networks
# Date: 02/03/2020
# Lab3: Server support for multiple clients
# Goal: Learning Networking in Python with TCP sockets
# Student Name: Jonathan McGrath
# Student ID: 918145233
# Student Github Username: JonOct 45
# Lab Instructions: No partial credit will be given. Labs must be completed in class, and must be committed to your
#               personal repository by 9:45 pm.
# Running instructions: This program needs the server to run. The server creates an object of this class.
#
########################################################################################################################

import threading
import pickle



class ClientHandler:
    """
    The client handler class receives and process client requests
    and sends responses back to the client linked to this handler.
    """

    def __init__(self, server_instance, clienthandler, addr):
        """
        Class constructor already implemented for you.
        :param server_instance: passed as 'self' when the object of this class is created in the server object
        :param clientsocket: the accepted client on server side. this handler, by itself, can send and receive data
                             from/to the client that is linked to.
        :param addr: addr[0] = server ip address, addr[1] = client id assigned buy the server
        """
        self.server_ip = addr[0]
        self.client_id = addr[1]
        self.server = server_instance
        self.handler = clienthandler
        self.print_lock = threading.Lock()  # creates the print lock
        self.sendID(self.client_id)

    def process_requests(self):
        """
        TODO: Create a loop that keeps waiting for client requests.
              Note that the process_request(...) method is executed inside the loop
              Recall that you must break the loop when the request received is empty.
        :return: VOID
        """
        while True:

            #We will need to serialize the data
            request = self.receive()

            if not request:
                break

            #When the request is empty, we will break
            self.process_request(request)
      

    def process_request(self, request):
        """
        TODO: This implementation is similar to the one you did in the method process_request(...)
              that was implemented in the server of lab 3.
              Note that in this case, the clienthandler is not passed as a parameter in the function
              because you have a private instance of it in the constructor that can be invoked from this method.
        :request: the request received from the client. Note that this must be already deserialized
        :return: VOID
        """
        
        if self.handler:
            self.log(f'Connected: Student: {request["student_name"]}, Github Username: {request["github_username"]}, sid: {request["sid"]}')
            
        else:
            self.log("Failed to processm, {}".format(self.handler))
        
        pass  # remove this line after this method is implemented.

    def send(self, data):
        """
        TODO: serializes data with pickle, and then send the serialized data
        """
        #Serializing the Data
        serialized = pickle.dumps(data)

        #Sending the serialized data
        self.handler.send(serialized)
        

    def receive(self, max_mem_alloc=4096):
        """
        TODO: receive the data, deserializes the data received
        :max_mem_alloc: an integer representing the maximum allocation (in bytes) in memory allowed
                        for the data that is about to be received. By default is set to 4096 bytes
        :return: the deserialized data
        """

        serialized_data = self.handler.recv(max_mem_alloc)

        if serialized_data:

            deserialized_data = pickle.loads(serialized_data)
        else:
            deserialized_data = 0
            
        return deserialized_data

    def sendID(self, clientid):
        """
        TODO: send the client id to the client
        """
        data = {'clientid': clientid}

        self.send(data)


    def log(self, message):
        """
        TODO: log a message on the server windows.
              note that before calling the print statement you must acquire a print lock
              the print lock must be released after the print statement.
        """

        self.print_lock.acquire()

        #Printing message 
        print(message)

        self.print_lock.release()


    def run(self):
        """
        Already implemented for you
        """
        self.process_requests()
