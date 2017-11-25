#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import os
import json
import logging.config


def setup_logging( default_path = os.path.join(os.getcwd(), 'logger/logger_configurations.json'), default_level = logging.INFO):
    """
    Function that initialize the logger.
    :param default_path: path where read the conf
    :param default_level: default level of logging
    :return: --
    """

    if os.path.isfile(default_path):

        with open(default_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)

    else:

        logging.basicConfig(level=default_level)

    return