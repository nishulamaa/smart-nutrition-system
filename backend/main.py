from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn

from database.db import get_db
from services.engine import RecommendationEngine
from schemas import MealResponse, FoodItem


app = FastAPI(
    title="NutriSmart API",
    description="Smart Nutrition & Meal Recommendation System for University Students",
    version="1.0.0"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Recommendation Engine
# =========================

recommender = RecommendationEngine()


# =========================
# Home
# =========================

@app.get("/")
def read_root():
    return {
        "system": "NutriSmart API",
        "status": "Online",
        "version": "1.0.0"
    }


# =========================
# Analyze Food
# =========================

@app.post("/api/analyze-food", response_model=MealResponse)
async def analyze_food(
    file: Optional[UploadFile] = File(None),
    budget: int = Form(10000),
    time_limit: int = Form(15),
    preference: str = Form("balanced"),
    db: Session = Depends(get_db)
):

    # Check uploaded image
    if file:

        allowed_types = [
            "image/jpeg",
            "image/png",
            "image/webp"
        ]

        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=400,
                detail="Invalid file type. Only JPEG, PNG and WEBP are allowed."
            )

    # Recommendation
    result = recommender.analyze_and_recommend(
        budget=budget,
        max_time=time_limit,
        preference=preference
    )

    return result


# =========================
# Get All Foods
# =========================

@app.get("/api/foods", response_model=List[FoodItem])
def get_all_foods(
    db: Session = Depends(get_db)
):

    return recommender.get_all_student_meals()


# =========================
# Run Server
# =========================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )