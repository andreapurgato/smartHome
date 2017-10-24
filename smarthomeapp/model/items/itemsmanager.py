#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import os
import json
from jinja2 import Environment, PackageLoader
from smarthomeapp.model.items import ITEMS_PARAMS


class ItemsManager:
    """ Class representing the Home model """

    _ITEM_CFG_PATH = os.path.join(os.getcwd(), os.path.join('configurations', 'items'))

    def __init__(self):
        """  Model Constructor """
        self._items = [] # all the items of the smart home
        self._load_items() # load all the items

        return


    def _load_items(self):
        """
        Function used to load all the items from configuration files.
        :return: --
        """

        # environment used to load all the JSON
        env = Environment(loader=PackageLoader('smarthomeapp', 'configurations/items'))
        env.filters['jsonify'] = json.dumps # set the JSON type

        log.info("Loading all the items of the home present at path: " + self._ITEM_CFG_PATH)
        for item_cfg_filename in os.listdir(self._ITEM_CFG_PATH):

            # create template and load it
            template = env.get_template(item_cfg_filename)
            item_cfg_content = template.render(items=ITEMS_PARAMS)
            log.info("loaded " + item_cfg_filename + "\n" + item_cfg_content)

            # manage the item characteristics coming from the JSON


        return



