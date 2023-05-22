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

USERNAME = 'Jorge'

KAOMOJIS = ['(≧◡≦) ♡','♡(>ᴗ•)','૮ ˶ᵔ ᵕ ᵔ˶ ა']

TELEGRAM = {
    'API_KEY' : config('API_KEY_TELEGRAM'),
    'CHAT_ID' : config('CHAT_ID_TELEGRAM'),
    'WEBHOOK_URL' : config('WEBHOOK_URL'),
}


# TODO: IN MAINTENANCE

TEMPLATES = {
    'x4leqxinn' : '-`♡´- Mi Creador 死神 ૮ ˶ᵔ ᵕ ᵔ˶ ა',
    'midas' : 'Jugando con el midas',
    'krishna' : 'Te quiero ૮ ˶ᵔ ᵕ ᵔ˶ ა  -`♡´-',
    'help' : '[x] !help',
    'start' : '[♡] ¡Hola {username}! {kaomoji}'.format(
        username=USERNAME,
        kaomoji=KAOMOJIS[rand(0,len(KAOMOJIS)-1)]
    ),
    '' : '',
}

COMMANDS = {
    '!help' : TEMPLATES.get('help'),
    '!x4leqxinn' : TEMPLATES.get('x4leqxinn'),
    '!krishna' : TEMPLATES.get('krishna'),

}

#print(TEMPLATES.get('start'))



TAGS_METADATA = [
    {
        "name": "webhooks",
        "description": "webhooks endpoints"
    }
]