from fastapi import FastAPI
from recommon import Recommender

app = FastAPI()

# Инициализация модели рекомендаций
recommender = Recommender()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/recommend")
def get_recommendations(user_id: str):
    # Пример получения рекомендаций
    recommendations = recommender.recommend(user_id)
    return {"recommendations": recommendations}
