from decouple import config

TELEGRAM = {
    'API_KEY' : config('API_KEY_TELEGRAM'),
    'CHAT_ID' :  config('CHAT_ID_TELEGRAM')
}
