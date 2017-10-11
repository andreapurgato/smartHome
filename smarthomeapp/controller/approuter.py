#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

from flask import Flask
from smarthomeapp.controller import appcontroller



# app instance
SMART_HOME_APPLICATION = Flask(__name__)
CONTROLLER = None

def setup_application():
    """ 
    Function that create a controller instance and start the smarthomeapp.
    :return: --
    """

    global SMART_HOME_APPLICATION, CONTROLLER

    SMART_HOME_APPLICATION.run()
    appcontroller.Controller()

    return


# ----------------------------------------
# routing requests
# ----------------------------------------

@SMART_HOME_APPLICATION.route('/')
def home_page():
    """
    Home page returned.
    :return: home page instance.
    """

    return 'Hello World!'