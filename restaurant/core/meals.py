from restaurant.core.database import RestaurantDatabase


class Meals(RestaurantDatabase):
    def __init__(self):
        super().__init__()
        self.table = "meals"

    def add_meal(self, meal):
        command = '''INSERT INTO meals(name, unit, type, recipe)
                     VALUES(?,?,?, ?) '''
        return self.execute_command(command, meal)

    def add_meal_type(self, meal_type):
        command = 'INSERT INTO meal_types(name) VALUES(?) '
        return self.execute_command(command, (meal_type,))

    def add_serving_unit(self, serving_unit):
        command = 'INSERT INTO serving_unit(name) VALUES(?) '
        return self.execute_command(command, (serving_unit,))

    def add_recipe(self, recipe):
        command = 'INSERT INTO recipes(name) VALUES(?)'
        return self.execute_command(command, (recipe,))

    def remove_recipe(self, recipe):
        command = 'DELETE FROM recipes WHERE id = ?'
        return self.execute_command(command, (recipe,))

    def remove_meal(self, meal):
        command = 'DELETE FROM meals WHERE id = ?'
        self.execute_command(command, (meal,))

    def remove_meal_type(self, meal_type):
        command = 'DELETE FROM meal_types WHERE id = ?'
        self.execute_command(command, (meal_type,))

    def remove_serving_unit(self, serving_unit):
        command = 'DELETE FROM meal_types WHERE id = ?'
        self.execute_command(command, (serving_unit,))

    def get_meal_type(self, meal):
        if type(meal) == str:
            meal = self.get_meal_id(meal)
        query = ''' SELECT t.name
                    FROM meal_types t
                    INNER JOIN meals m on t.id = m.type 
                    WHERE m.id = ?'''
        rows = self.execute_command(query, (meal,))
        return rows[0]["name"]

    def get_meal_id(self, item):
        query = '''SELECT id FROM meals WHERE name = ?'''
        rows = self.execute_command(query, (item,))
        return rows[0]["id"]


meals = Meals()
