import logging
from config import Config
from psycopg_pool import ConnectionPool

logger = logging.getLogger(__name__)

class DBManager:
    def __init__(self, config:Config):
        self.config:Config = config
        self.pool:ConnectionPool = None

    def init(self):
        db_config = {
            "host": self.config.get("db.host", "localhost"),
            "dbname": self.config.get("db.name", "postgres"),
            "user": self.config.get("db.username", "postgres"),
            "password": self.config.get("db.password"),
            "port": self.config.get("db.port", "5432") 
        }

        self.pool = ConnectionPool(
            "host={host} dbname={dbname} user={user} password={password} port={port}".format(**db_config),
            min_size = self.config.get_int("db.pool.min_size", 1),  
            max_size = self.config.get_int("db.pool.max_size", 1)
        )
        
        self.pool.wait(timeout=5)
        
        logging.info("connection pool ready")
        
        return self
    
    def get_connection(self):
        return self.pool.connection()

    def close_pool(self):
        self.pool.close()

    