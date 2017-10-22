#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import threading

class RequestManager(threading.Thread):


    def __init__(self, group=None, target=None, name=None,  args=()):
        """ Request Manager Constructor """
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.queue = args[0] # queue used to get all the requests
        self.controller = args[1] # controller instance
        return


    def run(self):
        """ Run function of the thread """
        log.info("Request Manager started")

        while True:

            log.info("Waiting request from user...")
            self.queue.get()
            log.info("Got request from user, processing it")

            continue


    def manage_requests(self, request=None):
        """
        Function that manage all the requests that comes from the user
        :param request: request made by the user to be processed
        :return: --
        """

        return



class Request:
    """ Class used to contains all the requests sent by the user """

    def __init__(self, request=""):
        """ Request Constructor """
        self.request = request
        return
