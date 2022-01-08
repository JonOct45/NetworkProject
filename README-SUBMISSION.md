        Project Readme.
        NAME: Jonathan McGrath
        SID: 918145233
        GIT: JonOct45
        Version: Python 3.6
        External Libraries: Sockets

TCP/UDP Protocols
    
        The Project is to use TCP and UDP Protocols to perform various menu options given by the server. The ClientHandler and ClientHelper are both communicating in order to achieve this transmission of data between the server and client. The server supports multiple Clients and upon creation of the ClientHandler, generates a ClientID for the Client, and moderates interaction with the Menu and the Headers. The ClientHelper facilitates the data that is being sent between both classes, then displays the data to the client, or the Server will send and display the data to the client. The Headers from the Menu are to be instructions on how to send and recieve data.

        Challenges - Resolves

1.  The initial structure of the Project was confusing, and reading through discord helped to clear somethings up. I get easily confused and caught up sometimes, a little overwhelmed when doing large coding projects and when especially learning multiple things at once.

        This was semi resolved as I watched more lectures and read Discord. Later on, talking through the arcitecture, I was able to draw out and took a step back to see the larger picture. Practicing patience and doing things in small steps while taking breaks has helped. Unfortunately not so much for the Milestone.

2.  Since I did not complete Lab4, which I did at a later time. It was challenging to get my Server and Client working with Threads, and since the Project depends on the Server.py to be completed from Lab4, this caused delays and later on more confusion when attempting the Project. This and other outside contributors prolonged

        I was able to complete Lab4 past the due date and was able to connnect multiple clients. Once they were connected, it was much easier and some data was passed as normal. Also ensuring my environment supports quiet and concentration contributed to me being able to work harder on the project, even if it was late.

3.  Getting Data Structures down, such as Dictionaries, List Iteration, Class - Inheritance proved to be challenging as I tried to access each and properly utilize attributes of each Class.

        While reading and rewatching lectures proved to be useful for the Project, I was not able to catch up to speed enough, but I did learn many valuable tools and resources that helped me understand and create more streamlined code. I later on discovered the Basic.py file and used it to clear some things up. Rewatching lectures helped and I Was able to utilize more datastructures

4.  Threading proved to be also challenging, even though I took 415, I was having many race conditions and errors on my project when attempting to access critical areas. I was unsure on where they should be.

        This resolve took a while and complicated my code as I was getting more and more tangled responses and requests. I was able to utilize by removing all locks, and put the Locks on the ClientHandler in the Run() and that fixed all of the race conditions I had on the Server Side. As you can see I used a lot of print statements to trace where I was at in my code, this helped comb out a lot of content and errors, it also allowed me to generate stronger methods. I was able to get my Option 4 to work with the use of threads, but the data was consistently on the server. 

5.  Receiving and Sending headers. I realized that I had a lot of attributes and methods that were not uniform and were making things complicated. This brought up more frustration, and with out utilizing some Test Methods that were in ClientHelper, I was not able to completely create Menu processing out of the Client.

        This resolve took the entire project as I removed and implimented Methods, in some cases complicating things. Towards the end, I was able to get a more clear concise set of methods and attributes that I could use. I later discovered a different way of getting information to the client as they connected. This is where I sent the Menu and the ID. 

        

6. Manipulating the Server Handlers list proved challenging. I was able to convey data to the server and to other clients, but the formatting was tangled as my limited knowledge of dictionaries. It was also difficult to compare objects as some of the values and keys were integers or strings. 
        
        This resolve was as I familiarized myself more with the data structures, I Was able to manipulate the attributes on the client handlers where I could store and receive messages. 

PHOTOS:

This is the Connection of Multiple Clients, all with Menus and Server acknowledging. I also create the UDP object here.

![Alt text](/Project/photos/Logging.png?raw=true "CONNECTING")

This is the initial Options Photos.  

![Alt text](/Project/photos/Option1.png?raw=true "Getting Lists")



This is the User List and MEssages. Format for both were difficult due to my initial update to the dictionary upon starting the server. The username was there but ommited as the Dict got tangled with Keys. 

![Alt text](/Project/photos/Option3.png?raw=true "Messages / Deleting")
![Alt text](/Project/photos/Option4.png?raw=true "UDP Errors")