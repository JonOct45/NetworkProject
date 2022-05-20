        Project Readme.
        NAME: Jonathan McGrath
        SID: 918145233
        GIT: JonOct45
        Version: Python 3.6
        External Libraries: Sockets



Option #1 - Get Users List

        Retreiving the Users list by accessing the ClientHandlers list of users. Displaying the Lists Names and ClientIDs.
        The list is stored on the server and contains a Clienthandler object of each user signed in. 


Option #2 - Send a Message

        Asking the Client to input the Sender, Message and the Recipient. Messages are stored on the ClientHandler of the recepient.
        
Option #3 - Get My Messages

        Retrieves Messages that are stored on the ClientHandler, Displays the Header and Message.

Option #4 - Send a Direct message with UDP Protocol

        Created a file from class called UDP_Socket.py that will facilitate the creation and transmission of UDP

Option#5 - Broadcast a messge with CDMA Protocol

        Created a file CDMA_Protocol that Generates Codes / Encodes / EncodesAll. Methods in the CDMA_Protocol are static and facilitate generating the codes for users and decoding. 
        The Class / Methods worked but the architecture of the program proved challenging in Decoding messages for Clients. 


Option #6 - Get the Routing Table of the Server

        The Routing table is generated everytime a user picks this option. It sends a new Matrix to each user and sends them a string which displays the Network Map


Option #7 - Get the Network Routing Table with LinkState Protocol

        The Routing table Matrix is used to calculate the distance from the host user to every user using the LinkState Protocol


Option #8 - Get the Network Routing Table with the Distance Vector Protocol

        The Routing table Matrix is used to calculate the distance from the host to every user using the Distance Vector Protocol. 

Option #9 - Exit the Server

        The Client is closed from the server, from the Server side and all data of the user is deleted. 
