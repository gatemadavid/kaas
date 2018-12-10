class User():
    """
    This is a class that defines the base user methods
    """

    def __init__(self, username, lastLoggedIn, isLoggedIn=False):
        self.isLoggedIn = isLoggedIn
        self.username = username
        self.lastLoggedInAt = lastLoggedIn


class Moderator(User):
    def delete_comment(self):
        return True

class Admin(Moderator):
    """ admin class, inherits from Moderator, adds abiliity to edit any comment """
    def __init__(self):
        super(Moderator, self).__init__()

    def editComment(self):
        if isLoggedIn = True:
            return True
