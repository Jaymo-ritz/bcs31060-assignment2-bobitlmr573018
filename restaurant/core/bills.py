from restaurant.core.database import RestaurantDatabase


class Bills(RestaurantDatabase):
    def __init__(self):
        super().__init__()
        self.table = "bills"

    def add_bill(self, bill):
        command = '''INSERT INTO bills(service_number, charge, paid, balance, date)
                     VALUES(?,?,?,?,?) '''
        self.execute_command(command, bill)

    def get_bill(self, service_number):
        query = '''SELECT
                       charge,
                       paid,
                       balance,
                       date
                  FROM bills
                  WHERE service_number = ?'''
        result = self.execute_command(query, (service_number,))[0]
        return result


bills = Bills()
