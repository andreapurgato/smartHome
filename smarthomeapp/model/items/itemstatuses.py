#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import abc
from smarthomeapp.model.items.itemsutils import ItemException, OnOff

# -----------------------------------------------------
#                 Abstract Status
# -----------------------------------------------------

class Status():
    """ Abstract class of the item status """
    __metaclass__ = abc.ABCMeta # this is an abstract class

    def __init__(self, value):
        """ 
        Constructor 
        :param value: value to assign to the status value
        """
        self._value = value
        return

    def get_value(self):
        """
        :return: the current status.
        """
        return self._value

    def __str__(self):
        """ Function used to print the status """
        return str(self.get_value())


# -----------------------------------------------------
#             Implemented Status Classes
# -----------------------------------------------------

class OnOffStatus(Status):
    """ Enum class used for ON/OFF types items """

    def __init__(self, value):
        """Constructor
        :param status: initial status of the item
        :raise ItemException: if the status given is not instance of the ON/OFF enum
        """

        if value is OnOff.OFF or value is OnOff.ON:
            Status.__init__(self, value)
        else:
            raise ItemException("Wrong OnOffStatus status given, status " + str(value) + ' not recognised')
        return




class GradientStatus(Status):
    """ Class used for Gradient types items """

    def __init__(self, value):
        """
        Constructor
        :param status: initial status of the item, can only be from 0 to 100
        :raise ItemException: if the status is not coherent with above description
        """

        if isinstance(value, int) and value >= 0 and value <= 100:
            Status.__init__(self, value)
        else:
            raise ItemException("Wrong GradientStatus status given, status " + str(value) + ' not accepted')
        return
