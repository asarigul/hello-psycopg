import logging
from lifecycle import Lifecycle
from config import Config
from dbmanager import DBManager
from service.itemservice import ItemService

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)-15s - %(levelname)-8s - %(threadName)-15s - %(message)s')

logger = logging.getLogger(__name__)

class Application:
    def __init__(self):
        self.lifecycle:Lifecycle = Lifecycle()
        self.config:Config = Config()
        self.dbmanager:DBManager = None


    def start(self):
        logger.info("starting app")
        self.dbmanager = DBManager(self.config).init()
        self.lifecycle.on_exit(self.dbmanager.close_pool)
        
        self.service = ItemService(self.dbmanager)

        self.service.create_item('test', 'description')



application = Application()
application.start()

