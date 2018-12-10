import datetime

class User():
    """
    This is a class that defines the base user methods
    """

    def __init__(self, username, lastLoggedIn, isLoggedIn=False):
        self.isLoggedIn = isLoggedIn
        self.username = username
        self.lastLoggedInAt = lastLoggedIn

    def logIn(self):
        """
        Method signs in a user by setting loggedIn property to true and
        updating user lastLoggedInAt timestamp

        Returns
        -------
        None
        """

        self.isLoggedIn = True
        self.lastLoggedInAt = datetime.datetime.today().strftime('%Y/%m/%d - %I:%M%p')
        return None

class Moderator(User):
    def delete_comment(self):
        return True
