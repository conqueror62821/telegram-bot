from decouple import config
from .command_templates import *
from .openapi_metadata import *
from .commands import *

DEBUG = config('DEBUG',cast=bool,default=True)

if DEBUG:
    from dotenv import load_dotenv
    load_dotenv('.env.dev')
else:
    from dotenv import load_dotenv
    load_dotenv('.env.prod')

HOST = config('HOST')


TELEGRAM = {
    'API_KEY' : config('API_KEY_TELEGRAM'),
    'CHAT_ID' : config('CHAT_ID_TELEGRAM'),
    'WEBHOOK_URL' : config('WEBHOOK_URL'),
}


GIPHY = {
    'API_KEY' : config('GIPHY_API_KEY'),
    'GIF_BASE_URL' : 'https://api.giphy.com/v1/gifs',
    'STICKER_BASE_URL' : 'https://api.giphy.com/v1/stickers',
}


TIMEZONE = 'Chile/Continental'


ALLOW_ORIGINS = ['http://0.0.0.0:8000']
ALLOW_CREDENTIALS = True
ALLOW_METHODS = ['*']
ALLOW_HEADERS = ['*']
EXPOSE_HEADERS = ''
MAX_AGE = ''