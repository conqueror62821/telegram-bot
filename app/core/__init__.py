from fastapi import FastAPI
import uvicorn
from core.manage import settings
from api.v1.controllers.telegram_bot_webhook import webhooks_router

# Start APP 
app = FastAPI(docs_url="/api-docs")

# Routers
app.include_router(webhooks_router, prefix="/api/v1")


def run_server(): uvicorn.run(app, host=settings.HOST, port=8000)
