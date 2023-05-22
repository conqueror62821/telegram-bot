from fastapi import Request
import telegram
from core.routers import webhooks_router
from models.telegram_custom_bot import TelegramCustomBot
import websockets
import json

bot = TelegramCustomBot()

@webhooks_router.post(
    "/webhook-messages",
    tags=["webhooks"],
    response_model=None,
    description="Telegram messages webhook.",
)
async def webhook(request: Request):
    update = telegram.Update.de_json(await request.json(), bot)
    message = update.message

    # Skip messages
    if message.message_id == bot.last_message_id: return
    
    # Process
    bot.last_message_id = message.message_id
    bot.current_message = message

    data = {'response' : True,'chat_id': bot.last_message_id}

    # send data to WebSocket
    async with websockets.connect('ws://0.0.0.0:8000/ws') as websocket:
        await websocket.send(json.dumps(data))

    return {'status' : 'OK'}
