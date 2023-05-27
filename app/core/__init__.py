from fastapi import FastAPI 
import uvicorn
from starlette.responses import RedirectResponse
from core.manage import settings
from fastapi.middleware.cors import CORSMiddleware
import json
from core.logger import logger
from .global_events import setup_global_events
from .websockets import setup_ws
from .routers import setup_routes

origins = ["http://0.0.0.0:8000"]

app = FastAPI(
    title="Telegram Bot API",
    description="a REST API using python for Telegram Bot",
    version="0.0.1",
    openapi_tags=settings.TAGS_METADATA,
    openapi_url="/openapi",
    docs_url='/docs',
    redoc_url='/redocs',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

setup_global_events(app)
setup_ws(app)
setup_routes(app)

def start():
    logger.info('Start server')
    uvicorn.run('core:app',host=settings.HOST,port=8000,reload=True)
