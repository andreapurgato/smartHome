#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import threading

class SessionController(threading.Thread):
    """ Class that manages all the requests that comes from the User GUI """

    def __init__(self, group=None, target=None, name=None,  args=()):
        """ Request Manager Constructor """
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.setName("RequestManager")

        # get params
        self._request_session_queue = args[0] # queue used to get all the requests
        return


    def run(self):
        """ Run function of the thread """
        log.info("Session Controller started")

        while True:

            log.info("Waiting session request...")
            self._request_session_queue.get()
            log.info("Got session request, processing it")

            # TODO: MANAGE THE SESSION REQUEST

            continue



    def _manage_requests(self, request=None):
        """
        Function that manage all the requests that comes from the user
        :param request: request made by the user to be processed
        :return: --
        """

        return




