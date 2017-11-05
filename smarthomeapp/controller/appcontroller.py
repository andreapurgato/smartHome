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
from smarthomeapp.model.items.itemsmanager import ItemsManager
from smarthomeapp.controller import approuter
from smarthomeapp.controller import requestmanager


# -----------------------------------------------------
#                   Initialize
# -----------------------------------------------------

def initialize_app():
    """
    Function used to initialize all the components of the application
    :return: --
    """

    # create object needed
    request_queue = Queue()

    # setup the item manager
    log.info('Initializing Items manager')
    items_manager = ItemsManager()

    # create system controller
    controller = Controller(items_manager=items_manager)
    controller.load_items()

    # setup the request manager
    log.info('Initializing Request manager')
    request_manager = requestmanager.RequestManager(args=[request_queue, controller])
    request_manager.setName('RequestManager') # set thread name
    request_manager.start() # start request manager thread

    # setup & start the Flask application
    log.info('Initializing Flask application')
    flask_application = threading.Thread(name='FlaskApplication', target=approuter.start_application, args=[request_queue])
    flask_application.start()

    log.info('End application initialization')

    return


# -----------------------------------------------------
#                   Controller
# -----------------------------------------------------

class Controller:
    """ Class representing the Home controller """

    _ITEM_CFG_PATH = os.path.join(os.getcwd(), os.path.join('configurations', 'items'))

    def __init__(self, request_queue = Queue(), items_manager = ItemsManager()):
        """
        Controller Constructor
        :param request_queue: queue of the request to be performed by the controller
        :param items_manager: model object of the system
        """
        self._request_queue = request_queue
        self._items_manager = items_manager
        return


    def load_items(self):
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
            self._items_manager.create_item(item_cfg_content['model'], item_cfg_content['name'])

        return


