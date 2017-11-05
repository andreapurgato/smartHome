#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

from smarthomeapp.model.items.itemsdefintion import *
from smarthomeapp.model.items.itemsutils import ItemException


class ItemsModel:
    """ Class representing the Home model """

    ITEM_ID = 0 # ID counter for the new ids

    def __init__(self):
        """  Model Constructor """
        self._items = {} # all the items of the smart home
        return


    def create_item(self, model, name):
        """
        Function used to add the item given to the model
        :param model: class to instantiate for the item requested.
        :param name: name of the item to create
        :return: --
        """

        item = eval(model)(self.ITEM_ID, name) # create the item

        # check if model is subclass of AbstractItems
        if not isinstance(item, AbstractItem):
            raise ItemException("Tried to add a non-item to the item manager map, class " + model + " not allowed")

        # add the item to the map and increase the id counter
        self._items[item.get_id()] = item
        log.debug("loaded item :\n" + str(item))

        self.ITEM_ID += 1

        return

    def get_items(self):
        """
        :return: the items map 
        """
        return self._items



