
import logging
from .repository import Repository
from dbmanager import DBManager

logger = logging.getLogger(__name__)

class ItemRepository (Repository):
    def __init__(self, db_manager:DBManager):
        super().__init__(db_manager)

    def create_item(self, name, description):
        with super()._connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
                conn.commit() 

    def read_items(self):
        with super()._connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM items")
                return cur.fetchall()
            
    def update_item(self, id, name, description):
        with super()._connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE items SET name = %s, description = %s WHERE id = %s", (name, description, id))
                conn.commit()
    


