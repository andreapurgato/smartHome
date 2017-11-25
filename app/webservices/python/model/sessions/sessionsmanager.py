#####################################
# Smart Home Project
# Author: Andrea Purgato
#####################################

import logging
log = logging.getLogger(__name__)

import time


# ----------------------------------------------------------------------------
#                            Session Manager
# ----------------------------------------------------------------------------

class SessionsManager:
    """ Class used to manage all the session opened by the user """

    def __init__(self):
        """ Constructor of the session manager """
        self._sessions = {}

    def get_session(self, id):
        """
        Function that returns the session associated to the id given.
        :param id: id of the session to return.
        :return: session object requested.
        """

    def add_session(self, session):
        """
        Function that add a new session to the list.
        :return: --
        """

        if not isinstance(session, Session):
            log.error("Session object given is not Session instance")
            return

        self._sessions[session.get_id()] = session



# ----------------------------------------------------------------------------
#                               Session
# ----------------------------------------------------------------------------

class Session:
    """ Function used to keep track of the session opened by the users. """

    _session_counter = 0

    def __init__(self, name):
        """ Constructor """
        self._id = self._session_counter
        self._name = name
        self._start_time = time.time()
        self._logged = False

        self._session_counter += 1

    def get_id(self):
        """
        Id getter
        :return: the id of the current session. 
        """
        return self._id

    def get_name(self):
        """
        Name getter.
        :return: the name of the current session.
        """
        return self._name

    def get_start_time(self):
        """
        Start time getter.
        :return: the starting time instant.
        """
        return self._start_time

    def is_logged(self):
        """
        Check if logged or not
        :return: True if logged, False otherwise.
        """
        return self._logged
