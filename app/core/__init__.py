from fastapi import FastAPI
import uvicorn
from starlette.responses import RedirectResponse
from core.manage import settings
from api.v1.controllers.telegram_bot_webhook import webhooks_router


# Start APP 
app = FastAPI(
        title="Telegram Bot API",
        description="a REST API using python for Telegram Bot",
        version="0.0.1",
        openapi_tags=settings.TAGS_METADATA,
        docs_url="/api-docs",
    )

# Redirect
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/api-docs")

# Routers
app.include_router(webhooks_router, prefix="/api/v1")

def run_server(): uvicorn.run('core:app',host=settings.HOST,port=8000,reload=True)
