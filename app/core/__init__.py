from fastapi import FastAPI
import uvicorn
from core.manage import settings
from api.v1.controllers.telegram_bot_webhook import webhooks_router
from api.v1.controllers.items import items_router

# Start APP 
app = FastAPI(docs_url="/api-docs")

# Routers
app.include_router(webhooks_router, prefix="/api/v1")
app.include_router(items_router, prefix="/api/v1")


def run_server(): uvicorn.run('core:app',host=settings.HOST,port=8000,reload=True)
