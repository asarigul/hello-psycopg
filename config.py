import logging
from dotenv import load_dotenv
import os

logger = logging.getLogger(__name__)

class Config:
    def __init__(self):
        dotenv_path = os.getenv('ENV_FILE_PATH', 'dev.env')
        load_dotenv(dotenv_path=dotenv_path)
        logger.info("loaded env")
        

    def get(self, name, default = None):
        val = os.getenv(name)
        if val != None:
            return val
        
        return default
    
    def get_int(self, name, default = None):
        val_str = self.get(name)
        if val_str != None:
            return int(val_str)
        return default



