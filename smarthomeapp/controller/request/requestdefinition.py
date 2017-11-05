#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

class Request:
    """ Class used to contains all the requests sent by the user """

    def __init__(self, request=""):
        """ Request Constructor """
        self.request = request
        return