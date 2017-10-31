#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import os
import json
from smarthomeapp.model.items.itemsdefintion import * # import all the items classes


class ItemsManager:
    """ Class representing the Home model """

    _ITEM_CFG_PATH = os.path.join(os.getcwd(), os.path.join('configurations', 'items'))

    def __init__(self):
        """  Model Constructor """
        self._items = {} # all the items of the smart home
        self._load_items() # load all the items

        return


    def _load_items(self):
        """
        Function used to load all the items from configuration files.
        :return: --
        """

        # environment used to load all the JSON

        log.info("Loading all the items of the home present at path: " + self._ITEM_CFG_PATH)
        item_id = 0
        for item_cfg_filename in os.listdir(self._ITEM_CFG_PATH):

            # open the current config file
            log.debug('loading ' + item_cfg_filename + ' item config file')
            item_cfg_content = json.load(open(os.path.join(self._ITEM_CFG_PATH, item_cfg_filename)))

            # create Item object
            item_object = eval(item_cfg_content['model'])(item_id, item_cfg_content['name'])
            self._items[item_id] = item_object # add the item to the items map
            log.info("loaded " + item_cfg_filename + " :\n" + str(item_object))

            item_id += 1 # increase the items ids



        return



