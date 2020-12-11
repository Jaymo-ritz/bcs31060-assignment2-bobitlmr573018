from restaurant.core.database import RestaurantDatabase


class Patron(RestaurantDatabase):
    def __init__(self):
        super().__init__()
        self.table = "patron"

    def new_patron(self, patron):
        command = '''INSERT INTO patron(name, table_number)
                VALUES(?,?) '''
        return self.execute_command(command, patron)

    def get_name(self, service_number):
        query = '''SELECT name
                 FROM patron
                 WHERE service_number = ?
                 '''
        rows = self.execute_command(query, (service_number,))
        if len(rows) > 1:
            return rows[0]["name"]
        return None

    def get_table(self, service_number):
        query = '''SELECT table_number
                 FROM patron
                 WHERE service_number = ?
                 '''
        rows = self.execute_command(query, (service_number,))
        return rows[0]["table_number"] or None

    def patron_exists(self, service_number):
        return self.get_name(service_number) is not None


patron = Patron()
