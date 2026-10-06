
CREATE DATABASE smart_nutrition;

USE smart_nutrition;

CREATE TABLE food (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    food_name VARCHAR(100) NOT NULL,
    calories FLOAT NOT NULL,
    protein FLOAT NOT NULL,
    carbohydrates FLOAT NOT NULL,
    price FLOAT NOT NULL
);

INSERT INTO food
(food_name, calories, protein, carbohydrates, price)
VALUES
('Chicken Rice', 500, 30, 60, 5.00),
('Bibimbap', 550, 20, 70, 7.00),
('Tuna Sandwich', 350, 25, 40, 4.00),
('Vegetable Salad', 250, 10, 30, 3.50),
('Kimbap', 400, 15, 55, 3.00);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE recommendation (
    recommendation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    food_id INT NOT NULL,
    budget FLOAT,
    available_time INT,
    preference VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (food_id) REFERENCES food(food_id)
);

SHOW TABLES;

SELECT * FROM food;