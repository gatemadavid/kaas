class User():
    """
    This is a class that defines the base user methods
    """
    def __init__(self, username, lastLoggedIn, isLoggedIn=False):
        self.isLoggedIn = isLoggedIn
        self.username = username
        self.lastLoggedInAt = lastLoggedIn
