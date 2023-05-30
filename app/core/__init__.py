from fastapi import FastAPI 
import uvicorn
from core.manage import settings
from fastapi.middleware.cors import CORSMiddleware
from core.logger import logger
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio
import os
import time
from fastapi.responses import RedirectResponse
from fastapi import WebSocket,FastAPI
from starlette.websockets import WebSocketDisconnect
import json
from core.logger import logger

class CustomFastAPI(FastAPI):

    def __init__(self):
        kwargs = \
        {
            'title' : 'Telegram Bot API',
            'description' : 'a REST API using python for Telegram Bot',
            'version' : '0.0.1',
            'openapi_tags' : settings.TAGS_METADATA,
            'openapi_url' : '/openapi',
            'docs_url' : '/docs',
            'redoc_url' : '/redocs',
        }     
        super().__init__(**kwargs)
        self.configure()
    
    """GETTERS"""
    @property
    def server_timezone(self): return self.__server_timezone

    @property
    def scheduler(self): return self.__scheduler

    @scheduler.setter
    def scheduler(self,scheduler: BackgroundScheduler): 
        self.__scheduler = scheduler

    def configure(self):
        # Config app
        self.setup_server_timezone()
        self.setup_middlewares()
        self.setup_base_routes()
        self.setup_routes()
        self.setup_events()
        #self.setup_ws()
        #self.init_scheduler()


    def setup_server_timezone(self):
        tz = settings.TIMEZONE
        os.environ['TZ'] = tz
        time.tzset()
        self.__server_timezone = tz
        logger.info(f'SERVER TIME ZONE SETTER {tz}')

    def setup_middlewares(self):
        self.add_middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOW_ORIGINS,
            allow_credentials=settings.ALLOW_CREDENTIALS,
            allow_methods=settings.ALLOW_METHODS,
            allow_headers=settings.ALLOW_HEADERS,
            expose_headers=settings.EXPOSE_HEADERS,
            max_age=settings.MAX_AGE,
        )
        logger.info('MIDDLEWARES SET') 

    def setup_base_routes(self):
        
        """MAIN PATH"""
        @self.get("/", include_in_schema=False)
        async def root(): return RedirectResponse(url="/docs")

    def setup_routes(self):
        """API ROUTER"""
        from fastapi import APIRouter
        from api.v1.controllers import telegram_bot_webhook
        
        global_router = APIRouter()
        global_router.include_router(telegram_bot_webhook.router,prefix=settings.VERSION.get(1))
        
        self.include_router(global_router, prefix="/api")
        logger.info('API ROUTES SET')

    def set_task_scheduler(self):
        self.scheduler = BackgroundScheduler()

    def init_scheduler(self): pass
    """
        self.set_task_scheduler()
        from core.tasks import exec_async
        self.scheduler.add_job(exec_async,'interval', minutes=1)
        self.scheduler.start()
        logger.info('TASK SCHEDULER RUNNED')
    """

    def setup_events(self):
        """GLOBAL EVENTS"""
        @self.on_event("startup")
        async def startup_event():
            logger.info('RUN SERVER')

        @self.on_event("shutdown")
        async def shutdown():
            logger.info('SHUTDOWN SCHEDULER')
            #self.scheduler.shutdown()

    def setup_ws(self):
        @self.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            try:
                await websocket.accept()

                while True: pass
                    # Get data
                    #data = await websocket.receive_text()
                    #print('a',data,type(data))
                    

 
            except WebSocketDisconnect as e:
                print("Diconnect websocket:", e)


    
app = CustomFastAPI()


def start():
    uvicorn.run('core:app',host=settings.HOST,port=8000,reload=True)
