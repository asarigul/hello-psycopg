import atexit
import logging


logger = logging.getLogger(__name__)

class Lifecycle:
    def __init__(self):
        self.__shutdown_callbacks = []
        atexit.register(self.__on_exit)

    def on_start(self, f):
        pass

    def on_exit(self, func:callable, params:list = None):
        if params == None:
            params = []

        self.__shutdown_callbacks.append((func, params))

    def __on_exit(self):
        logger.warning("Application is shutting down...")

        for (func, params) in self.__shutdown_callbacks:
            logger.info("calling %s", func.__name__)
            try:
                func(*params)
            except Exception as e:
                print(e)


    