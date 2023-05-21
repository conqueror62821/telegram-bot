from fastapi import FastAPI, Request
import uvicorn
from TelegramCustomBot import TelegramCustomBot
from settings import HOST, COMMANDS
import telegram


app = FastAPI()
bot = None

def start_bot():
    # Initialize
    global bot
    bot = TelegramCustomBot()
    print("Start bot")


async def startup_event():
    start_bot()

@app.on_event("startup")
async def on_startup():
    await startup_event()


@app.post("/webhook-messages")
async def webhook(request: Request):
    update = telegram.Update.de_json(await request.json(), bot)
    message = update.message
    
    if message.message_id == bot.last_message_id: return
    
    # Process
    bot.last_message_id = message.message_id
    bot.current_message = message
    #from datetime import datetime

    print(bot.current_message.date)
    print(bot.current_message.from_user.first_name)
    print(bot.current_message.from_user.last_name)
    print(bot.current_message.text)
    await bot.send_message()

    return {'status' : 'OK'}

if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=8000)
