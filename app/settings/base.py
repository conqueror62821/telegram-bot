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



