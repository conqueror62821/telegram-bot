from core.logger import logger
from core.manage import settings 
from telegram import Update, Bot, Message, BotCommand
import asyncio


class TelegramHandler:
    __instance = None
    __LOOP = asyncio.get_event_loop()
    __TOKEN: str = settings.TELEGRAM.get('API_KEY')
    __bot: Bot = Bot(token=__TOKEN)
    __current_message: Message
    __webhook_url: str = settings.TELEGRAM.get('WEBHOOK_URL')
    __user = None
    __is_command = False
    __commands:list[BotCommand] = []


    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__LOOP.create_task(cls._configure()) # Start bot
            logger.info('Start bot')
        return cls.__instance

    @property
    def bot(self):
        return self.__bot

    @property
    def current_message(self):
        return self.__current_message
    
    @current_message.setter
    def current_message(self, message: Message):
        self.__current_message = message

    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def is_command(self):
        return self.__is_command
    
    @is_command.setter
    def is_command(self, is_command):
        self.__is_command = is_command

    @classmethod
    async def _configure(cls):
        # setup webhook url
        await cls.__bot.set_webhook(url=TelegramHandler.__webhook_url)
        # setup commands
        await cls._commands_setup()

    @staticmethod
    def _set_commands():        
        for key in settings.COMMANDS.keys():
            command = settings.COMMANDS[key]['command']
            TelegramHandler.__commands.append(command)     

    @staticmethod
    async def _commands_setup():
        TelegramHandler._set_commands()
        await TelegramHandler.__bot.set_my_commands(TelegramHandler.__commands)


    async def call_command(self,command: str):
        if settings.COMMANDS[command]['type'] == 'reply_text':
            await self.current_message.reply_text(text=settings.COMMANDS[command]['function'])
        elif settings.COMMANDS[command]['type'] == 'custom':
            await settings.COMMANDS[command]['function'](self.bot,self.current_message.chat_id)
            



    async def _handle_commands(self):
        found = False

        for command in self.__commands:
            if command.command == self.current_message.text: 
                found = True 
                break
        
        if found:
            # Execute
            await self.call_command(command.command)
        else:
            await self.current_message.reply_text('Ese comando esta ausente como tu papá:v')

    def _verify_message(self):
        self.is_command = False
        if self.current_message.entities: 
            if str(self.current_message.entities[0].type) == 'bot_command': self.is_command = True


    def _handle_chat(self):
        # Group or Private CHAT
        if self.current_message.chat.type == 'group':
            response = f'{ self.current_message.from_user.first_name } k wea ctm'
        elif self.current_message.chat.type == 'private': pass
            #response: str  = self.handle_response(text)
           # await update.message.reply_text(response)
        
    async def handle_message(self, update: Update):
        # Set current message update
        self.current_message = update.message
        self.user = update.message.from_user

        self._verify_message()

        # Command message
        if self.is_command:
            await self._handle_commands()
        # Response message
        else:
            print('No es un comando')
        return True




telegram_app = TelegramHandler()