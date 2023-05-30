from fastapi import Request,APIRouter,status,HTTPException,UploadFile,File,Form
import telegram
import websockets
import json
from core.logger import logger
from fastapi.responses import Response
from core.manage import settings 
from pydantic import BaseModel, validator,root_validator
from typing import Optional
from telegram import Update
from telegram.ext import *


from models.telegram_handler import telegram_app

# TODO: Refac endpoints api
class BaseMessage(BaseModel):
    chat_id: Optional[str] 

    @property
    def model_name(self) -> str: return 'message'
    
    @root_validator(pre=True)
    def validate_fields(cls, values):
        chat_id = values.get('chat_id')
        if not chat_id: 
            values['chat_id'] = settings.TELEGRAM.get('CHAT_ID')
        return values

class RequiredTextMessage(BaseMessage):
    text: str

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
    update = Update.de_json(await request.json(), telegram_app.bot)
    response = await telegram_app.handle_message(update)
    if not response: raise HTTPException(status_code=400, detail="The request could not be processed")
    return Response(status_code=204)


@router.post(
    '/telegram/bot/send_message',
    response_model=None,
    description='Send message from bot.',
)
async def send_telegram_message(message: RequiredTextMessage):
    print(message.chat_id)
    response = await telegram_app.bot.send_message(chat_id=message.chat_id,text=message.text)
    if not response: raise HTTPException(status_code=400, detail="Message not sent")
    content = json.dumps(
        {
            'response': True,
            'message': f'Message sent sucessfully.',
            'body': {
                message.model_name : message.dict()
            }
        }
    )
    return Response(status_code=201,content=content, media_type="application/json")

