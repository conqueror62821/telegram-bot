from fastapi import APIRouter,FastAPI
from api.v1.controllers import telegram_bot_webhook
from core.manage import settings

# Global routers
def setup_routes(app : FastAPI):
    global_router = APIRouter()
    global_router.include_router(telegram_bot_webhook.router,prefix=settings.VERSION.get(1))
    app.include_router(global_router, prefix="/api")