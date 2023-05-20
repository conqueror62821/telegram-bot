from telegram import Bot
from settings import TELEGRAM
import asyncio

class TelegramCustomBot:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.bot = Bot(token=TELEGRAM.get('API_KEY'))
        return cls.__instance

    @property
    def instance(self):
        return self.__instance

    async def send_message(self,message):
        await self.__instance.bot.send_message(chat_id=TELEGRAM.get('CHAT_ID'), text=message)



asyncio.run(TelegramCustomBot().send_message(message='Test'))