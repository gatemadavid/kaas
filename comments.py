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

def editComment(self, author, comment_id, message):
    author = self.author
    if loggedinUser == author:
        for comment in comments:
            if comment['id'] == comment_id:
                comment['message'] = message
    else:
        return {"Message": "You cannot edit this comment. You are not the owner."}
