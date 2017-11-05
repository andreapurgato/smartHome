#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

import threading
from Queue import Queue
from smarthomeapp.controller.app import approuter
from smarthomeapp.model.items.itemsmodel import ItemsModel
from smarthomeapp.controller.app.usercontroller import UserController
from smarthomeapp.controller.app.itemscontroller import ItemsController
from smarthomeapp.controller.app.itemsupdater import ItemsUpdater


# -----------------------------------------------------
#                   Initialize
# -----------------------------------------------------

def initialize_app():
    """
    Function used to initialize all the components of the application
    :return: --
    """

    # create object needed
    user_queue = Queue() # queue used for all the requests coming from the users
    request_queue = Queue() # queue used for all the requests to be made to the Items Controller

    # setup the item manager
    log.info('Initializing Items Model')
    items_model = ItemsModel()

    # setup the request manager
    log.info('Initializing User Request Manager')
    user_controller = UserController(args=[user_queue, request_queue])
    user_controller.start()

    # create system items controller
    log.info('Initialize the Items Controller')
    items_controller = ItemsController(args=[request_queue, items_model])
    items_controller.start()

    # setup & start the Flask application
    log.info('Initializing Flask application')
    flask_application = threading.Thread(name='FlaskApplication', target=approuter.start_application, args=[user_queue])
    flask_application.start()

    log.info('End application initialization')

    return