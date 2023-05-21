import os
from importlib import import_module
settings_module = os.environ.get('BOT_SETTINGS_MODULE', 'settings.development')
settings = import_module(settings_module)
# core.manage import settings