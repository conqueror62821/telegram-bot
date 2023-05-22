from fastapi import Request
import telegram
from core.routers import webhooks_router
from models.telegram_custom_bot import TelegramCustomBot

bot = TelegramCustomBot()

@webhooks_router.post(
    "/webhook-messages",
    tags=["webhooks"],
    response_model=None,
    description="Telegram messages webhook.",
)
async def webhook(request: Request):
    print("BOTSITO",bot)

    update = telegram.Update.de_json(await request.json(), bot)
    message = update.message

    print(message.message_id)
    # Skip messages
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
