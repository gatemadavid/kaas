"""
Comments file
"""
import datetime
COMMENTS = []
REPLIES = []


class Comment(object):
    """
    Comment class used to create a comment isinstance

    Properties
    ----------
    message : String
    timestamp : datetime String
    author : object of user class
    """

    def __init__(self, message, author):
        """
        Constructor to initialize a comment created by a user/author
        """
        self.message = message
        self.author = author
        self.timestamp = datetime.datetime.now()


class Reply():
    """
    Reply class used to create a reply isinstance

    Properties
    ----------
    message_id : Int
    reply_id : Int
    reply : String (reply message)
    """
    def __init__(self, reply, message_id):
        self.message_id = message_id
        self.id_counter = len(REPLIES)
        self.reply_id = self.id_counter + 1
        self.reply = reply
