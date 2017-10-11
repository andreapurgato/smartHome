#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import logger
from smarthomeapp.controller import approuter


def main():
    """  The main routine """

    logger.setup_logging()

    log.info("Starting Smart Home Project server...")
    approuter.setup_application()



if __name__ == "__main__":
    main()