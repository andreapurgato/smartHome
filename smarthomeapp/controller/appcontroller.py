#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

import threading
from Queue import Queue
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

    # create object instances needed
    controller = Controller()
    request_queue = Queue()

    # setup the request manager
    log.info('Initializing Request manager')
    request_manager = requestmanager.RequestManager(args=[request_queue, controller])
    request_manager.setName('RequestManager') # set thread name
    request_manager.start() # start request manager thread

    # setup the items manager

    # setup the Flask application
    log.info('Initializing Flask application')
    flask_application = threading.Thread(name='FlaskApplication', target=approuter.start_application, args=[request_queue])
    flask_application.start()

    return


# -----------------------------------------------------
#                   Controller
# -----------------------------------------------------

class Controller:
    """ Class representing the Home controller """

    def __init__(self):
        """ Controller Constructor """
        return


