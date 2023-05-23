from decouple import config
from random import randint as rand

DEBUG = config('DEBUG',cast=bool,default=True)

if DEBUG:
    from dotenv import load_dotenv
    load_dotenv('.env.dev')
else:
    from dotenv import load_dotenv
    load_dotenv('.env.prod')

HOST = config('HOST')

KAOMOJIS = ['(≧◡≦) ♡','♡(>ᴗ•)','૮ ˶ᵔ ᵕ ᵔ˶ ა']

TELEGRAM = {
    'API_KEY' : config('API_KEY_TELEGRAM'),
    'CHAT_ID' : config('CHAT_ID_TELEGRAM'),
    'WEBHOOK_URL' : config('WEBHOOK_URL'),
}


# TODO: IN MAINTENANCE


COMMANDS = {
    '!help' : TEMPLATES.get('help'),
    '!x4leqxinn' : TEMPLATES.get('x4leqxinn'),
    '!krishna' : TEMPLATES.get('krishna'),

}


TEMPLATES = {
    'x4leqxinn' : '-`♡´- Mi Creador 死神 ૮ ˶ᵔ ᵕ ᵔ˶ ა',
    'midas' : 'Jugando con el midas',
    'krishna' : 'Te quiero ૮ ˶ᵔ ᵕ ᵔ˶ ა  -`♡´-',
    'help' : '[x] !help',
    '' : '',
}


TAGS_METADATA = [
    {
        "name": "webhooks",
        "description": "webhooks endpoints"
    }
]