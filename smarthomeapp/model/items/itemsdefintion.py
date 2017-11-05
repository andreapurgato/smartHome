#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

from abc import ABCMeta
from smarthomeapp.model.items.itemstatuses import OnOffStatus, GradientStatus, Status
from smarthomeapp.model.items.itemsutils import ItemException, OnOff


# -----------------------------------------------------
#                   Abstract Item
# -----------------------------------------------------

class AbstractItem:
    """ Abstract class of the items loaded in the system """
    __metaclass__ = ABCMeta # this is an abstract class

    def __init__(self, id, name):
        """
        Constructor
        :param id: id of the current item
        :param name: name of the light item
        """
        self._id = id
        self._name = name
        self._status = None
        return


    def __str__(self):
        """ Function used to print the status """
        return  "id : " + str(self._id) + "\n" \
                "type : " + str(type(self)) + "\n" \
                "name : " + str(self._name) + "\n" \
                "status : " + str(self._status)


    def get_id(self):
        """
        Function that return the ID of the item
        :return: item id
        """
        return self._id

    def get_name(self):
        """
        Function that return the name of the item
        :return: item name
        """
        return self._name


    def get_status(self):
        """
        Function that returns the status of the current item
        :return: item status
        """
        return self._status


# -----------------------------------------------------
#                   Light Items Classes
# -----------------------------------------------------

# ------------------ Light superclass -----------------
class Light(AbstractItem):
    """ Item class used for lights """
    __metaclass__ = ABCMeta # this is an abstract class

    def __init__(self, id, name):
        """
        Constructor
        :param id: id of the current item
        :param name: name of the light item
        """
        AbstractItem.__init__(self, id, name)
        return



# ----------------- On/Off Light class -----------------
class OnOffLight(Light):
    """ Class used for On/Off light items """

    def __init__(self, id, name):
        """
        Constructor
        :param id: id of the current item
        :param name: name of the light item
        """
        Light.__init__(self, id, name) # call base class constructor
        self._status = OnOffStatus(OnOff.OFF)# initialize the status as OFF
        return



# ---------------- Gradient Light class ----------------
class GradientLight(Light):
    """ Class used for Gradient light items """

    def __init__(self, id, name):
        """
        Constructor
        :param id: id of the current item
        :param name: name of the light item
        """
        Light.__init__(self, id, name) # call base class constructor
        self._status = GradientStatus(0) # initialize the status as 0
        return



