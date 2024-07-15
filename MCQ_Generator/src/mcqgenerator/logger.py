"""
A logging setup script for the 'mcqgenerator' package.

This script configures logging for the 'mcqgenerator' project. It creates a
directory for log files if it doesn't exist and sets up a log file with a 
timestamp in its name. The logging configuration includes the log level, 
log file, and log message format.

The log file is named using the current date and time to ensure unique log 
files for each run.

Attributes:
    LOG_FILE (str): The path to the log file, including a timestamp in the name.
    LOG_PATH (str): The directory path where the log file will be stored.
"""

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
