#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

import threading
from Queue import Queue
from app.webservices.python.controller.app import approuter
from app.webservices.python.model.items.itemsmodel import ItemsModel
from app.webservices.python.controller.app.sessioncontroller import SessionController
from app.webservices.python.controller.app.itemscontroller import ItemsController


# -----------------------------------------------------
#                   Initialize
# -----------------------------------------------------

def initialize_app():
    """
    Function used to initialize all the components of the application
    :return: --
    """

    # create objects needed
    request_queue = Queue() # queue used for all the requests
    request_items_queue = Queue() # queue used by the request dispatcher to send all the request items related
    request_session_queue = Queue() # queue used used by the request dispatcher to send all the request session related

    # ------ step 1: build model
    # create items model and sessions model
    log.info('Initializing Items Model')
    items_model = ItemsModel()
    # session_model = SessionModel()


    # ------ step 2: create items controller
    # create system items controller
    log.info('Initialize the Items Controller')
    items_controller = ItemsController(args=[request_items_queue, items_model])
    items_controller.start()


    # ------ step 3: create session controller
    # create system sessions controller
    log.info('Initializing Session Controlelr')
    # user_controller = SessionController(args=[request_session_queue, session_model])
    user_controller = SessionController(args=[request_session_queue])
    user_controller.start()


    # # setup & start the Flask application
    log.info('Initializing Flask application')
    flask_application = threading.Thread(name='FlaskApplication', target=approuter.start_application, args=[request_queue])
    flask_application.start()

    log.info('End application initialization')

    return