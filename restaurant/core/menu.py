from restaurant.core.database import RestaurantDatabase


class Menu(RestaurantDatabase):
    def __init__(self):
        super().__init__()
        self.table = "menu"

    def add_item(self, item):
        command = '''INSERT INTO menu(item, price, available_servings)
                VALUES(?,?,?) '''
        self.execute_command(command, item)

    def remove_item(self, item):
        command = 'DELETE FROM menu WHERE item = ?'
        self.execute_command(command, (item,))

    def update_item_quantity(self, item, available_servings):
        command = '''UPDATE menu
                    SET available_servings = available_servings + ?
                    WHERE item = ?
                    '''
        self.execute_command(command, (item, available_servings))

    def update_item_price(self, item, new_price):
        command = '''UPDATE menu
                    SET price =  ?
                    WHERE item = ?
                    '''
        self.execute_command(command, (item, new_price))

    def get_item_price(self, item):
        query = "SELECT price FROM menu WHERE item = ?"
        rows = self.execute_query(query, (item,))
        return rows[0]['price']

    def get_available_servings(self, item):
        query = "SELECT available_servings FROM menu WHERE item=?"
        rows = self.execute_query(query, (item,))
        return rows[0]['available_servings']

    def can_order_item(self, item, servings):
        query = "SELECT  FROM items WHERE id=?"
        rows = self.execute_query(query, (item,))
        return rows[0]['available_servings'] >= servings

    def get_items(self, item_type):
        if type(item_type) == str:
            item_type = self.get_item_type_id(item_type)

        query = '''SELECT
                    m.name,
                    i.price
                FROM menu i
                INNER JOIN meals m ON i.item = m.id
                WHERE m.type = ?
                '''
        rows = self.execute_query(query, (item_type,))
        return rows

    def get_item_types(self):
        query = '''SELECT * FROM meal_types'''
        rows = self.execute_query(query)
        return rows

    def get_item_type(self, item):
        query = '''SELECT name FROM meal_types WHERE id = ?'''
        rows = self.execute_query(query, (item,))
        return rows[0]["name"]

    def get_item_type_id(self, item_type):
        query = '''SELECT id FROM meal_types WHERE name = ?'''
        rows = self.execute_query(query, (item_type,))
        return rows[0]["id"]


menu = Menu()

