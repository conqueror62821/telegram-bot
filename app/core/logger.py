import os
import logging
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

current_date = datetime.now().strftime("%Y-%m-%d")

relative_path = '../../logs/'
logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

log_file_path = os.path.join(logs_dir, f'logs-{current_date}.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
