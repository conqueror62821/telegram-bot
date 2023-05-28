import os
import logging
from datetime import datetime

class Logger:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if hasattr(self, 'initialized'): return
        self.initialized = True
        self.config()

    def config(self):
        self.format_setup()
        self.logger_setup()
        self.stream_handler_setup()
        self.file_handler_setup()

    def stream_handler_setup(self):
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.INFO)
        self.stream_formatter = logging.Formatter(fmt=self.log_format)
        self.stream_handler.setFormatter(self.stream_formatter)
        self.logger.addHandler(self.stream_handler)

    def file_handler_setup(self):
        self.file_handler = logging.FileHandler(self.log_file_path)
        self.file_handler.setLevel(logging.INFO)
        self.formatter = logging.Formatter(fmt=self.log_format)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def format_setup(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s"
        self.relative_path = '../../logs/'
        self.logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), self.relative_path))
        self.log_file_path = os.path.join(self.logs_dir, f'logs-{self.current_date}.log')
        
    def logger_setup(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
"""Start logger"""
logger = Logger().logger