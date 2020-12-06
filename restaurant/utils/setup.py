from restaurant.core.meals import meals
from restaurant.core.menu import menu
from restaurant.core.database import database as db


def setup_example_db():
    db.reset_database()

    default_recipe = meals.add_recipe("default")
    default_serving = meals.add_serving_unit("serving")

    starter = meals.add_meal_type('starter')
    main_course = meals.add_meal_type('main course')
    dessert = meals.add_meal_type('dessert')
    drink = meals.add_meal_type('drink')

    meal_items = (
        ("Cream of Tomato Soup", default_serving, starter, default_recipe),
        ("Beef Soup and Toast", default_serving, starter, default_recipe),
        ("Chicken Soup and Bread", default_serving, starter, default_recipe),
        ("Spicy Bean Salad", default_serving, starter, default_recipe),

        ("Rice and Beef", default_serving, main_course, default_recipe),
        ("Chips and Chicken", default_serving, main_course, default_recipe),
        ("Chapati and Lentils", default_serving, main_course, default_recipe),
        ("Spanish Omelette", default_serving, main_course, default_recipe),
        ("Ugali Kale and Beef", default_serving, main_course, default_recipe),
        ("Spaghetti and Meat Balls", default_serving, main_course, default_recipe),

        ("Chocolate Cake", default_serving, dessert, default_recipe),
        ("Samosas", default_serving, dessert, default_recipe),
        ("Chocolate Pancakes", default_serving, dessert, default_recipe),
        ("Apple Pie", default_serving, dessert, default_recipe),

        ("Tea", default_serving, drink, default_recipe),
        ("Coffee", default_serving, drink, default_recipe),
        ("Soft Drink", default_serving, drink, default_recipe),
        ("Sparkling Water", default_serving, drink, default_recipe),
        ("Iced Tea", default_serving, drink, default_recipe),
        ("Milkshake", default_serving, drink, default_recipe),
        ("Water", default_serving, drink, default_recipe)
    )

    for meal in meal_items:
        meal_id = meals.add_meal(meal)
        menu.add_item((meal_id, 100, 100))


if __name__ == '__main__':
    setup_example_db()
