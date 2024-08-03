from fastapi import FastAPI
from recommon import Recommender

app = FastAPI()

# Инициализация модели рекомендаций
recommender = Recommender()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
