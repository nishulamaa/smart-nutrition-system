from fastapi import FastAPI
import mysql.connector

app = FastAPI()


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="smart_nutrition"
    )


@app.get("/")
def home():
    return {"message": "Smart Nutrition API is working"}


@app.get("/foods")
def get_foods():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM food")
    foods = cursor.fetchall()

    cursor.close()
    db.close()

    return foods