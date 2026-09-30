from fastapi import FastAPI
from schemas import NutritionResponse

app = FastAPI(
    title="Smart Nutrition System",
    description="Backend API for a Smart Nutrition System for University Students",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Smart Nutrition System API is running!",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/nutrition/sample", response_model=NutritionResponse)
def sample_nutrition():
    return {
        "food_name": "Kimbap",
        "calories": 450,
        "protein": 12,
        "carbohydrates": 65,
        "fat": 15,
        "serving_size": "1 roll"
    }