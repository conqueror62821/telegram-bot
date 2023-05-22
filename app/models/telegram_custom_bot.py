from telegram import Bot
from core.manage import settings 
import asyncio
import time

class TelegramCustomBot:
    __instance = None
    __LOOP = asyncio.get_event_loop()

    @staticmethod
    async def _set_url():
        print('RESETEO')
        await TelegramCustomBot.__instance.bot.set_webhook(url=settings.TELEGRAM.get('WEBHOOK_URL'))

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.bot = Bot(token=settings.TELEGRAM.get('API_KEY'))
            cls.__LOOP.create_task(cls._set_url()) # Thread
        return cls.__instance

    def __init__(self, last_message_id=None):
        self.__last_message_id = last_message_id
        self.__attempts = 0

    @property
    def instance(self):
        return self.__instance

    @property
    def command(self): return self.__command

    @command.setter
    def command(self,command):
        self.__command = command if (command in settings.COMMANDS.keys()) else 'default'

    @property
    def last_message_id(self):
        return self.__last_message_id

    @last_message_id.setter
    def last_message_id(self,last_message_id):
        self.__last_message_id = last_message_id

    @property
    def current_message(self):
        return self.__current_message

    @current_message.setter
    def current_message(self,message):
        self.__current_message = message

    def _increase_failed_attempts(self):
        self.__attempts += 1

    def _reset_failed_attempts(self):
        self.__attempts = 0

    def _verify_command(self) -> str:
        if self.__command != 'default': return self._get_template()
        self._increase_failed_attempts()
        return self._get_failed_message(self.__attempts)

    def _get_failed_message(self,attempts):
        switch = {
            1: 'test',
            2: 'test',
            3: 'test',
            4: 'test',
            5: 'test'
        }
        message = switch.get(attempts,None)

        if not message: 
            message = 'Superaste el limite de aweonamiento'
            self._reset_failed_attempts()
        return message

    def _get_template(self):
        return settings.COMMANDS.get(self.__command)

    async def send_message(self):
        self.command = self.current_message.text
        await self.__instance.bot.send_message(chat_id=settings.TELEGRAM.get('CHAT_ID'), text=self._verify_command())


