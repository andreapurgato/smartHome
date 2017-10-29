#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import abc
from enum import Enum
from smarthomeapp.model.items.itemsutils import ItemException


class Status():
    """ Abstract class of the item status """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """ Constructor """
        self._status = None
        return

    def get_status(self):
        """
        :return: the current status.
        """
        return self._status



class OnOffStatus(Status, Enum):
    """ Enum class used for ON/OFF types items """

    ON = 'ON'
    OFF = 'OFF'

    def __init__(self, status):
        """Constructor
        :param status: initial status of the item
        :raise ItemException: if the status given is not instance of the ON/OFF enum
        """
        Status.__init__(self)

        if status is self.OFF or status is self.ON:
            self._status = status
        else:
            raise ItemException("Wrong OnOffStatus status given, status " + status + ' not recognised')
        return


class GradientStatus(Status):
    """ Class used for Gradient types items """

    def __init__(self, status):
        """
        Constructor
        :param status: initial status of the item, can only be from 0 to 100
        :raise ItemException: if the status is not coherent with above description
        """
        Status.__init__(self)

        if isinstance(status, int) and status > 0 and status < 100:
            self._status = status
        else:
            raise ItemException("Wrong GradientStatus status given, status " + status + ' not accepted')
        return
