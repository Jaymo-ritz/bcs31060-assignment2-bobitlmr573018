from restaurant.core.database import RestaurantDatabase


class Patron(RestaurantDatabase):
    def __init__(self):
        super().__init__()
        self.table = "patron"

    def new_patron(self, patron):
        command = '''INSERT INTO patron(name, table_number)
                VALUES(?,?) '''
        return self.execute_command(command, patron)

    def get_name(self, patron):
        query = '''SELECT name
                 FROM patron
                 WHERE service_number = ?
                 '''
        rows = self.execute_query(query, (patron,))
        return rows[0]["name"] or None

    def get_table(self, patron):
        query = '''SELECT table_number
                 FROM patron
                 WHERE service_number = ?
                 '''
        rows = self.execute_query(query, (patron,))
        return rows[0]["table_number"] or None

    def patron_exists(self, patron):
        name = self.get_name(patron)
        return name is not None


patron = Patron()
