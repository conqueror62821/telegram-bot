from fastapi import Request,APIRouter,status
import telegram
import websockets
import json
from core.logger import logger
from fastapi.responses import Response
from core.init_bot import bot


router = APIRouter(
    prefix='/webhooks',
    tags=['Webhooks v1'],
    responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}}
)

@router.post(
    "/telegram-messages",
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
    
    logger.info(f'message received from {bot.current_message.from_user.first_name} {bot.current_message.from_user.last_name}.')

    # send data to WebSocket
    async with websockets.connect('ws://0.0.0.0:8000/ws') as websocket:
        await websocket.send(json.dumps(data))
    return Response(status_code=204)



