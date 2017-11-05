#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

from Queue import Queue
from smarthomeapp.model.items.itemsmanager import ItemsManager

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