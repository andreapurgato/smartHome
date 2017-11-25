#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

import os
from flask import Flask, send_from_directory
from jinja2 import Environment, PackageLoader



# app instance
SMART_HOME_APPLICATION = Flask(__name__)
USER_REQUEST_MANAGER = None


def start_application(args=None):
    """ 
    Function that create a controller instance and start the python.
    :param args: input arguments to the Thread
    :return: --
    """

    global SMART_HOME_APPLICATION, USER_REQUEST_MANAGER
    USER_REQUEST_MANAGER = args
    SMART_HOME_APPLICATION.run()

    return


# ----------------------------------------
# routing requests
# ----------------------------------------

@SMART_HOME_APPLICATION.route('/')
def home_page():
    """
    Home Page returned.
    :return: home page instance.
    """

    return ''