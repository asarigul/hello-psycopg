
import logging
from repo.item_repository import ItemRepository
from dbmanager import DBManager

logger = logging.getLogger(__name__)

class ItemService:
    def __init__(self, db_manager:DBManager):
        self.item_repository = ItemRepository(db_manager)

    def create_item(self, name, description):
        logger.info("creating item: name: %s, description: %s", name, description)
        self.item_repository.create_item(name, description)

    def read_items(self):
        return self.item_repository.read_items()
    
    def update_item(self, id, name, description):
        return self.item_repository.update_item(id, name, description)