#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import logger
import sys
import os
sys.path.append(os.path.dirname(__file__))

from app.webservices.python.controller.app import initialize_app


def main():
    """  The main routine """

    logger.setup_logging()

    log.info("Starting Smart Home Project server...")
    initialize_app()



if __name__ == "__main__":
    main()