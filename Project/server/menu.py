#######################################################################################
# File:             menu.py
# Purpose:          CSC645 Assigment #1 TCP socket programming
# Description:      Template Menu class. You are free to modify this
#                   file to meet your own needs. Additionally, you are
#                   free to drop this Menu class, and use a version of yours instead.
# IMPORTANT:        This file can only resides on the server side.
# Usage :           menu = Menu() # creates object
#
########################################################################################

class Menu:
    """
    IMPORTANT MUST READ: The Menu class is the user interface that acts as a communication bridge between the user
    and the Client-Server architecture of this application. The Menu is always located on the Server side (machine running the server).
    However, it must be printed on the Client console by the ClientHelper object. In order to accomplish this, students
    must create a
    """

    @staticmethod
    def get():
        """
        TODO: shows the following menu on the client side
        ****** TCP/UDP Network ******
        ------------------------------------
        Options Available:
        1.  Get users list
        2.  Send a message
        3.  Get my messages
        4.  Send a direct message with UDP protocol
        5.  Broadcast a message with CDMA protocol
        6.  Create a secure channel to chat with your friends using PGP protocol
        7.  Join an existing channel
        8.  Create a Bot to manage a future channel
        9.  Get the Routing Table of this client with Link State Protocol
        10. Get the Routing Table of this network with Distance Vector Protocol
        11. Turn web proxy server on (extra-credit)
        12. Disconnect from server
        """
        menu = ''' ****** TCP/UDP Network ******
        ------------------------------------
        Options Available:
        1.  Get users list
        2.  Send a message
        3.  Get my messages
        4.  Send a direct message with UDP protocol
        5.  Broadcast a message with CDMA protocol
        6.  Create a secure channel to chat with your friends using PGP protocol
        7.  Join an existing channel
        8.  Create a Bot to manage a future channel
        9.  Get network map
        10. Get the Routing Table of this client with Link State Protocol
        11. Get the Routing Table of this network with Distance Vector Protocol
        12. Turn web proxy server on (extra-credit)
        13. Disconnect from server'''
        # your code here
     
        return menu

    @staticmethod
    def option(self):
        """
        TODO: Ask the user to select an option from the menu
              Note. you must handle exceptions for options chosen that are not in the allowed range
        :return: an integer representing the option chosen by the user from the menu
        """
        while True:

            option = input("What is your option? : ")

            if option < 1 or option > 12:
                print("Not a valid option")
            else:
                break
  
        return option

    @staticmethod
    def request_headers():
        """
        TODO: In this method students implement the headers of the menu. That's it, the options the server expect
              for each requests from the client related to this menu. For example, the headers for option 2,
              the expected headers in a client request are {'option':<integer>, 'message':<string>, 'recipient':<integer>}
        """
        headers =  [{'option': 1, 'prompts': []}, 
                    {'option': 2, 'prompts': [("Enter your message: ", "message"), ('Entert recipient: ', 'recipient')], 'message': [], 'recipient': 0}, 
                    {'option': 3, 'prompts': []},
                    {'option': 4, 'prompts': [('Enter the address to bind your UDP client (e.g 127.0.0.1:6000): ', 'receive_address'),('Enter the recipient address: ', 'send_address'), ('Enter the message: ', 'message')]},
                    {'option': 5, 'prompts': [('Enter your message: ', 'message')], 'message': ''},
                    {'option': 6, 'prompts': []},
                    {'option': 7, 'prompts': []},
                    {'option': 8, 'prompts': []},
                    {'option': 9, 'prompts': []},
                    {'option': 10, 'prompts': []},
                    {'option': 11, 'prompts': []},
                    {'option': 12, 'prompts': []},
                    {'option': 13, 'prompts': []}]

        return headers

    @staticmethod
    def response_headers():
        """
        TODO: In this method students implement the headers of the menu. That's it, the options the server sends to
              the client for each response related to this menu. For example, the headers for the response of option 3
              are {'option':<integer>, 'messages':<Python Dictionary>}
        """
        headers = [
            {"header": "text", 'option': 1, 'body': ''}, 
            {"header": "text", 'option': 2, 'body': ''}, 
            {"header": "messages", 'option': 3, 'messages': []},
            {"header": "UDP", 'option': 4, 'body': ''},
            {"header": "text", 'option': 5, 'body': ''},
            {"header": "text", 'option': 6, 'body': ''},
            {"header": "text", 'option': 7, 'body': ''},
            {"header": "text", 'option': 8, 'body': ''},
            {"header": "text", 'option': 9, 'body': ''},
            {"header": "text", 'option': 10, 'body': ''},
            {"header": "text", 'option': 11, 'body': ''},
            {"header": "text", 'option': 12, 'body': ''},
            {"header": "exit", 'option': 13, 'body': ''}
            ]


        return headers

