from fastapi import WebSocket,FastAPI
from starlette.websockets import WebSocketDisconnect
import json
from core.logger import logger

from core.init_bot import bot

def setup_ws(app: FastAPI):
    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        try:
            await websocket.accept()

            while True:
                # Get data
                data_text = await websocket.receive_text()
                data_dict = json.loads(data_text)

                # Validate
                if data_dict.get('response',False) and int(data_dict.get('chat_id',0)) == bot.last_message_id:
                    await bot.send_message()
                    logger.info(f'Send message to {bot.current_message.from_user.first_name} {bot.current_message.from_user.last_name}.')

        except WebSocketDisconnect as e:
            print("Diconnect websocket:", e)

