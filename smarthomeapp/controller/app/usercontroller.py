#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import threading

class UserController(threading.Thread):
    """ Class that manages all the requests that comes from the User GUI """

    def __init__(self, group=None, target=None, name=None,  args=()):
        """ Request Manager Constructor """
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.setName("RequestManager")

        # get params
        self._user_queue = args[0] # queue used to get all the requests
        self._requests_queue = args[1] # queue used to put all the request that has to be managed by the items controller
        return


    def run(self):
        """ Run function of the thread """
        log.info("User Controller started")

        while True:

            log.info("Waiting request from user...")
            self._user_queue.get()
            log.info("Got request from user, processing it")

            # TODO: MANAGE USER REQUEST and PUT THE ITEM REQUEST TO THE _requests_queue

            continue



    def _manage_requests(self, request=None):
        """
        Function that manage all the requests that comes from the user
        :param request: request made by the user to be processed
        :return: --
        """

        return




