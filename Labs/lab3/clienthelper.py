# copy and paste your clienthelper.py code from lab2 here
class ClientHelper:

    def __init__(self, client):
        self.client = client
        self.student_name = 'Jonathan McGrath'  # TODO: your name
        self.student_id = 918145233 # TODO: your student id
        self.github_username = 'JonOct45'  # TODO: your github username

    def create_request(self, name, id, github_username):
        """
        TODO: create request with a Python dictionary to save the parameters given in this function
              the keys of the dictionary should be 'student_name', 'github_username', and
              'sid'.
        :return: the request created
        """

        #Creating the dictionary for request
        req_dictionary = {'student_name' : name, 'github_username' : github_username,
        'sid' : id}
        
        return req_dictionary

    def send_request(self, request):
        """
        TODO: send the request passed as a parameter
        :request: a request representing data deserialized data.
        """
        self.client.send(request)
        

    def process_response(self):
        """
        TODO: process a response from the server
              Note the response must be received and deserialized before being processed.
        :response: the serialized response.
        """

        #Returning the 
        self.client.receive()
       # print(data)
        #return data


       

    def start(self):
        """
        TODO: create a request with your student info using the self.request(....) method
              send the request to the server, and then process the response sent from the server.
        """

        #Calling the start() method
        request = self.create_request(self.student_name, self.student_id, self.github_username)
        self.send_request(request)
        self.process_response()
        #self.start()

       