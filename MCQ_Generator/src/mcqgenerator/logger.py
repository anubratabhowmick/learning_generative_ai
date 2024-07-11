import os
import logging
from datetime import datetime

LOG_FILE = f"mcq_generator_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_PATH = os.path.join(os.getcwd(), "logs")

os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(
    level = logging.INFO,
    filename = LOG_FILE,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

