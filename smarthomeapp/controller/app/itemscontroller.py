#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

import json
import os
import threading
from Queue import Queue
from smarthomeapp.model.items.itemsmodel import ItemsModel
from smarthomeapp.controller.app.itemsupdater import ItemsUpdater


# -----------------------------------------------------
#                   Controller
# -----------------------------------------------------

class ItemsController(threading.Thread):
    """ Class representing the Controller of all the items present in the system """

    _ITEM_CFG_PATH = os.path.join(os.getcwd(), os.path.join('configurations', 'items'))
    _ITEM_CHECK_PERIOD = 30.0

    def __init__(self, group=None, target=None, name=None, args=()):
        """ Items Controller Constructor """
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.setName("ItemsController")

        # get params
        self._request_queue = args[0]
        self._items_model = args[1]

        # load all the items
        self._load_items()

        # creates the items updater and start the periodic function
        self._items_updater = ItemsUpdater(self._request_queue)
        threading.Timer(0.0, self._update_items).start() # start check timer

        return


    def run(self):
        """ Run function of the thread """
        log.info("Items Controller started")

        while True:

            log.info("Waiting items request...")
            self._request_queue.get()
            log.info("Got request to items, processing it")

            # TODO: MANAGE ITEM REQUEST

            continue


    def _load_items(self):
        """
        Function used to load all the items from configuration files.
        :return: --
        """

        log.info("Loading all the items of the home present at path: " + self._ITEM_CFG_PATH)
        for item_cfg_filename in os.listdir(self._ITEM_CFG_PATH):

            # open the current config file
            log.debug('loading ' + item_cfg_filename + ' item config file')
            item_cfg_content = json.load(open(os.path.join(self._ITEM_CFG_PATH, item_cfg_filename)))

            # create and add the item to the model
            self._items_model.create_item(item_cfg_content['model'], item_cfg_content['name'])

        return



    def _update_items(self):
        """
        Periodic function that check the items status, use the ItemsUpdater object.
        :return: --
        """

        # update_catalog the status
        self._items_updater.check_items_status(self._items_model.get_items())

        # call the update every 30 seconds
        threading.Timer(self._ITEM_CHECK_PERIOD, self._update_items).start()
        return


