from models.custom_command import CustomCommand
from telegram import BotCommand

# TODO: Commads

COMMANDS = {
    '/help':{
        'command': BotCommand(command='/help', description='Lista de comandos disponibles ♡'),
        'function': CustomCommand.help_command(),
        'type': 'reply_text'
    },
    '/x4leqxinn':{
        'command': BotCommand(command='/x4leqxinn', description='♱𖤐⋆ Creador ૮ ˶ᵔ ᵕ ᵔ˶ ა'),
        'function': CustomCommand.creator_command(),
        'type': 'reply_text'
    },
    '/about':{
        'command': BotCommand(command='/about', description='Acerca de este bot (｡♡‿♡｡)'),
        'function': CustomCommand.about_command(),
        'type': 'reply_text'
    },
    '/onichan':{
        'command': BotCommand(command='/onichan', description='No lo hagas x tu salud mental ૮ ˶•~•˶ ა'),
        'function': CustomCommand.onichan_command,
        'type': 'custom'
    },
}

