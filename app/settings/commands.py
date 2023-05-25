from random import randint as rand

KAOMOJIS = ['(≧◡≦) ♡','♡(>ᴗ•)','૮ ˶ᵔ ᵕ ᵔ˶ ა']


# TODO: ADD NEW STATIC AND DYNAMIC COMMANDS
COMMANDS = {
    '!help' : {
        'description' : 'Listado de comandos.',
        'template' : '',
        'type' : 'dynamic'
    },
    '!x4leqxinn' : {
        'description' : 'Invoca una mona xina',
        'template' : f'Mi creador {KAOMOJIS[2]}',
        'type' : 'static',
    }
}