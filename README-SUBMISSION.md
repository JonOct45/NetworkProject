        Project Readme.
        NAME: Jonathan McGrath
        SID: 918145233
        GIT: JonOct45
        Version: Python 3.6
        External Libraries: Sockets

TCP/UDP Protocols
    
        The Project is to use TCP and UDP Protocols to perform various menu options given by the server. The ClientHandler and ClientHelper are both communicating in order to achieve this transmission of data between the server and client. The server supports multiple Clients and upon creation of the ClientHandler, generates a ClientID for the Client, and moderates interaction with the Menu and the Headers. The ClientHelper facilitates the data that is being sent between both classes, then displays the data to the client, or the Server will send and display the data to the client. The Headers from the Menu are to be instructions on how to send and recieve data.

        Challenges - Resolves



1. Getting Data Structures down, such as Dictionaries, List Iteration, Class - Inheritance proved to be challenging as I tried to access each and properly utilize attributes of each Class.

       
 

2. Receiving and Sending headers. I realized that I had a lot of attributes and methods that were not uniform and were making things complicated. This brought up more frustration, and with out utilizing some Test Methods that were in ClientHelper, I was not able to completely create Menu processing out of the Client.

        This resolve took the entire project as I removed and implimented Methods, in some cases complicating things. Towards the end, I was able to get a more clear concise set of methods and attributes that I could use. I later discovered a different way of getting information to the client as they connected. This is where I sent the Menu and the ID. 


PHOTOS:

This is the Connection of Multiple Clients, all with Menus and Server acknowledging. I also create the UDP object here.

![Alt text](/Project/photos/Logging.png?raw=true "CONNECTING")

This is the initial Options Photos.  

![Alt text](/Project/photos/Option1.png?raw=true "Getting Lists")



This is the User List and MEssages. Format for both were difficult due to my initial update to the dictionary upon starting the server. The username was there but ommited as the Dict got tangled with Keys. 

![Alt text](/Project/photos/Option3.png?raw=true "Messages / Deleting")
![Alt text](/Project/photos/Option4.png?raw=true "UDP Errors")
