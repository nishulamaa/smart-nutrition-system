from pydantic import BaseModel
from typing import Optional


class NutritionResponse(BaseModel):
    food_name: str
    calories: float
    protein: float
    carbohydrates: float
    fat: float
    serving_size: Optional[str] = None