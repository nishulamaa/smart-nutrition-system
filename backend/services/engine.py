class RecommendationEngine:

    def __init__(self):

        self.foods = [

            {
                "id": 1,
                "name": "Chicken Breast Rice",
                "calories": 520,
                "protein": 35,
                "carbs": 60,
                "price": 6500,
                "preparation_time": 10,
                "preference": "high-protein"
            },

            {
                "id": 2,
                "name": "Egg Sandwich",
                "calories": 350,
                "protein": 18,
                "carbs": 40,
                "price": 4500,
                "preparation_time": 5,
                "preference": "balanced"
            },

            {
                "id": 3,
                "name": "Tuna Salad",
                "calories": 300,
                "protein": 28,
                "carbs": 15,
                "price": 7000,
                "preparation_time": 8,
                "preference": "high-protein"
            },

            {
                "id": 4,
                "name": "Banana Yogurt",
                "calories": 220,
                "protein": 10,
                "carbs": 35,
                "price": 3500,
                "preparation_time": 3,
                "preference": "light"
            },

            {
                "id": 5,
                "name": "Vegetable Bibimbap",
                "calories": 450,
                "protein": 15,
                "carbs": 70,
                "price": 6000,
                "preparation_time": 12,
                "preference": "vegetarian"
            },

            {
                "id": 6,
                "name": "Kimbap",
                "calories": 420,
                "protein": 12,
                "carbs": 65,
                "price": 4000,
                "preparation_time": 5,
                "preference": "balanced"
            },

            {
                "id": 7,
                "name": "Chicken Salad",
                "calories": 380,
                "protein": 32,
                "carbs": 20,
                "price": 7500,
                "preparation_time": 10,
                "preference": "high-protein"
            },

            {
                "id": 8,
                "name": "Tofu Rice Bowl",
                "calories": 430,
                "protein": 20,
                "carbs": 55,
                "price": 5500,
                "preparation_time": 10,
                "preference": "vegetarian"
            },

            {
                "id": 9,
                "name": "Greek Yogurt & Fruit",
                "calories": 250,
                "protein": 15,
                "carbs": 30,
                "price": 5000,
                "preparation_time": 3,
                "preference": "light"
            },

            {
                "id": 10,
                "name": "Tuna Kimbap",
                "calories": 390,
                "protein": 22,
                "carbs": 55,
                "price": 5000,
                "preparation_time": 5,
                "preference": "balanced"
            }

        ]


    # =========================
    # Recommendation
    # =========================

    def analyze_and_recommend(
        self,
        budget: int,
        max_time: int,
        preference: str
    ):

        suitable_foods = []


        # First filter:
        # Budget + time + preference

        for food in self.foods:

            if (
                food["price"] <= budget
                and
                food["preparation_time"] <= max_time
            ):

                if preference == "balanced":

                    suitable_foods.append(food)

                elif food["preference"].lower() == preference.lower():

                    suitable_foods.append(food)


        # If no food matches preference,
        # search using budget and time only.

        if not suitable_foods:

            for food in self.foods:

                if (
                    food["price"] <= budget
                    and
                    food["preparation_time"] <= max_time
                ):

                    suitable_foods.append(food)


        # If still nothing is found,
        # search using budget only.

        if not suitable_foods:

            for food in self.foods:

                if food["price"] <= budget:

                    suitable_foods.append(food)


        # Nothing found

        if not suitable_foods:

            return {

                "food_name": "No suitable meal found",

                "calories": 0,

                "protein": 0,

                "carbs": 0,

                "price": 0,

                "preparation_time": 0,

                "preference": preference,

                "recommendation_reason":
                    "Try increasing your budget or available time."

            }


        # Select meal with highest protein

        selected = max(
            suitable_foods,
            key=lambda x: x["protein"]
        )


        return {

            "food_name": selected["name"],

            "calories": selected["calories"],

            "protein": selected["protein"],

            "carbs": selected["carbs"],

            "price": selected["price"],

            "preparation_time":
                selected["preparation_time"],

            "preference":
                selected["preference"],

            "recommendation_reason":
                f"This meal fits your "
                f"₩{budget:,} budget and "
                f"{max_time}-minute time limit."

        }


    # =========================
    # Get All Meals
    # =========================

    def get_all_student_meals(self):

        return self.foods