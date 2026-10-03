from pydantic import BaseModel


class FoodItem(BaseModel):

    id: int

    name: str

    calories: float

    protein: float

    carbs: float

    price: int

    preparation_time: int

    preference: str


class MealResponse(BaseModel):

    food_name: str

    calories: float

    protein: float

    carbs: float

    price: int

    preparation_time: int

    preference: str

    recommendation_reason: str