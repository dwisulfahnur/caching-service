from fastapi import FastAPI
from src.handlers import router

app = FastAPI(title='Caching Service')

app.include_router(router=router)
