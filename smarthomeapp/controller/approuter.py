#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

import os
from flask import Flask, send_from_directory
from jinja2 import Environment, PackageLoader
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
    Home Page returned.
    :return: home page instance.
    """

    page = Environment(loader = PackageLoader('smarthomeapp', 'view/templates')).get_template('home.html')
    return page.render()


@SMART_HOME_APPLICATION.route('/js/<path:path>')
def java_script(path):
    """
    JS requested returned.
    :return: JS file content.
    """

    return send_from_directory(os.path.join(os.getcwd(), 'view/js'), path)
