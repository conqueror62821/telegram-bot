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


from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler


def task():
    logger.info('Inicio de la tarea')
    # Aquí puedes definir la lógica de tu tarea programada
    print("¡Tarea programada ejecutada!")

# Crear una instancia del planificador
scheduler = BackgroundScheduler()

# Calcular el tiempo de inicio (5 minutos en el futuro)
start_time = datetime.now() + timedelta(minutes=1)

# Agregar la tarea programada al planificador con un retraso de inicio
scheduler.add_job(task, 'interval', minutes=1, start_date=start_time)

scheduler.start()



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
