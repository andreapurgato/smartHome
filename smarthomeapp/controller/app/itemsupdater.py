#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

from Queue import Queue

class ItemsUpdater():
    """ Class used to check the status of all the items periodically, so to update it """

    def __init__(self, request_queue = Queue()):
        """
        Constructor
        :param request_queue: queue of the request to be performed by the controller
        :param items_manager: items manager model
        """
        self._request_queue = request_queue
        return


    def check_items_status(self, items):
        """
        Function that loop over each items and check for the current status
        :return: --
        """

        # loop over each item and check the status
        for item_id in items:

            item = items[item_id] # get the item

            log.debug("Checking status of " + str(item.get_name()))

            # TODO: CHECK THE STATUS

            continue

        return

