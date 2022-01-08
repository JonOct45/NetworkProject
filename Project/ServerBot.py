"""
This will be the Bot for the server channels, 

Server Creates the bot with the users prefered settings, 

Name
Permissions
Channel

"""


class ServerBot:
    def __init__(self, name, permissions, channel):
        self.name = name
        self.permissions = permissions
        self.channel = channel

    def get_name(self):
        return self.name

    def get_permissions(self):
        return self.permissions

    def get_channel(self):
        return self.channel

    def BotHeader():
        header = """
        The disabled permissions for this bot are:
        1. Welcome users right after they join a channel. 
        2. Show a warning ot the users when they send words that not allowed. 
        3. Drop[ users from the channel after 3 warnings. 
        4. Compute the response time of a message when the user request it
        5. Inform the user when it has been inactive on the channel for more than 5 minutes.
        
        Enter an integer to enable a set of permissions:
        """

        return header

    