#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

from smarthomeapp.model.items import itemsmanager


class Controller:
    """ Class representing the Home controller """

    def __init__(self):
        """ Controller Constructor """
        self._model = itemsmanager.ItemsManager()
        return


