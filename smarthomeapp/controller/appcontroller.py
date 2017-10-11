#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import  logging
log = logging.getLogger(__name__)

from smarthomeapp.model import appmodel


class Controller:
    """ Class representing the Home controller """

    def __init__(self):
        """ Controller Constructor """
        self._model = appmodel.Model()
        return


