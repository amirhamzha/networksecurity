import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.Path.join(logs_path,LOG_FILE)

logging.basicConfig(

    filename=LOG_FILE_PATH,    
    format='%(asctime)s %(levelname)s -%(lineno)d - %(message)s',
    level=logging.INFO,  # Set to INFO; can change to DEBUG for detailed logs
)