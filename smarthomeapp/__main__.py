#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import logger
from smarthomeapp.controller import appcontroller


def main():
    """  The main routine """

    logger.setup_logging()

    log.info("Starting Smart Home Project server...")
    appcontroller.initialize_app()



if __name__ == "__main__":
    main()