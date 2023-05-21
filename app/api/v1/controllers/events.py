from models.telegram_custom_bot import TelegramCustomBot
from core.manage import settings

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
