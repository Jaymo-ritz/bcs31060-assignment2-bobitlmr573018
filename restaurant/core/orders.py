from restaurant.core.database import RestaurantDatabase


class Orders(RestaurantDatabase):
    def __init__(self):
        super().__init__()
        self.table = "orders"

    def add_order(self, order):
        if type(order[1]) == str:
            order = self._set_meal_id(order, 1)

        query = '''INSERT INTO orders(service_number, meal, servings)
                VALUES(?,?,?) '''
        self.execute_command(query, order)

    def remove_order(self, order):
        if type(order[0]) == str:
            order = self._set_meal_id(order, 0)

        command = '''DELETE FROM orders
                WHERE meal = ?
                AND service_number = ?
                '''
        self.execute_command(command, order)

    def update_order(self, order):
        if type(order[1]) == str:
            order = self._set_meal_id(order, 1)

        command = '''UPDATE orders
                SET servings = ?
                WHERE meal = ?
                AND service_number = ?
                '''
        self.execute_command(command, order)

    def get_orders(self, service_number):
        query = '''SELECT
                       m.name as item,
                       o.servings as servings,
                       i.price as price,
                       i.price * o.servings as total
                   FROM orders o
                   INNER JOIN meals m on m.id = o.meal
                   INNER JOIN menu i on m.id = i.item
                   WHERE o.service_number = ?
                '''
        rows = self.execute_command(query, (service_number,))
        return rows

    def total_orders_value(self, service_number):
        query = '''SELECT
                       SUM (i.price * o.servings) as total
                 FROM orders o
                 INNER JOIN menu i on o.meal = i.item
                 WHERE o.service_number = ?
                 '''
        rows = self.execute_command(query, (service_number,))
        return rows[0]["total"] or 0

    def get_meal_id(self, item):
        query = '''SELECT id FROM meals WHERE name = ?'''
        rows = self.execute_command(query, (item,))
        return rows[0]["id"]

    def _set_meal_id(self, order, index):
        order = list(order)
        order[index] = self.get_meal_id(order[index])
        return tuple(order)


orders = Orders()
