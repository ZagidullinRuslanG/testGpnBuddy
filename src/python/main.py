import uvicorn
from fastapi import FastAPI

from src.routers.predictor import predictor_router

app = FastAPI()

app.include_router(predictor_router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001, reload=True)
