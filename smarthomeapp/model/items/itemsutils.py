#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################


class ItemException(Exception):
    """ Exception used to raise errors from items """

    def __init__(self, message):
        """ Exception constructor """

        # call the base class constructor with the parameters it needs
        super(ItemException, self).__init__(message)