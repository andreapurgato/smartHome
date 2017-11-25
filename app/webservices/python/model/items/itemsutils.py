#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

from enum import Enum

class ItemException(Exception):
    """ Exception used to raise errors from items """

    def __init__(self, message):
        """ Exception constructor """

        # call the base class constructor with the parameters it needs
        super(ItemException, self).__init__(message)


class OnOff(Enum):
    """ Enum with the values of the ON/OFF status"""

    OFF = 'OFF'
    ON = 'ON'


    def __str__(self):
        """ Function used to custom print the Enum """
        return self.value