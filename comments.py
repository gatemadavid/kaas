"""
Comments file
"""
import datetime


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
