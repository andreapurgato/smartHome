#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import os


class ItemsManager:
    """ Class representing the Home model """

    _ITEM_CFG_PATH = os.path.join(os.getcwd(), 'configurations/items')

    def __init__(self):
        """ Model Constructor """
        self._items = [] # all the items of the smart home
        self._load_items() # load all the items

        return


    def _load_items(self):
        """
        Function used to load all the items from configuration files.
        :return: --
        """

        log.info("Loading all the items of the home...")
        for item_cfg_filename in os.listdir(self._ITEM_CFG_PATH):
            print item_cfg_filename

        return



