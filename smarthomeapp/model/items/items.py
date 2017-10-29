#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import abc
from smarthomeapp.model.items.itemstatuses import OnOffStatus, GradientStatus, Status
from smarthomeapp.model.items.itemsutils import ItemException


# -----------------------------------------------------
#                   Abstract Item
# -----------------------------------------------------

class AbstractItem:
    """ Abstract class of the items loaded in the system """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_status(self):
        """
        Function that returns the status of the current item.
        :return: item status.
        """
        return


# -----------------------------------------------------
#                   Light Items Classes
# -----------------------------------------------------

class Light(AbstractItem):
    """ Item class used for lights """
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        """
        Constructor
        :param name: name of the light item
        """

        self._name = name
        self._status = None
        return


    def get_status(self):
        """
        Function that returns the status of the current item.
        :return: item status.
        """

        # check is the status has the right instance
        if not issubclass(self._status, Status):
            raise ItemException('Wrong status instance, cannot return it. ' + self._status)

        return self._status



class OnOffLight(Light):
    """ Class used for On/Off light items """

    def __init__(self, name):
        """
        Constructor
        :param name: name of the light item
        """

        # call base class constructor
        Light.__init__(self, name)

        # initialize the status as OFF
        self._status = OnOffStatus(OnOffStatus.OFF)
        return



class GradientLight(Light):
    """ Class used for Gradient light items """

    def __init__(self, name):
        """
        Constructor
        :param name: name of the light item
        """

        # call base class constructor
        Light.__init__(self, name)

        # initialize the status as 0
        self._status = GradientStatus(0)
        return

