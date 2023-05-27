import os
import logging
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

current_date = datetime.now().strftime("%Y-%m-%d")
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s"

relative_path = '../../logs/'
logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

log_file_path = os.path.join(logs_dir, f'logs-{current_date}.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

stream_formatter = logging.Formatter(fmt=log_format)
stream_handler.setFormatter(stream_formatter)

logger.addHandler(stream_handler)

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(fmt=log_format)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
