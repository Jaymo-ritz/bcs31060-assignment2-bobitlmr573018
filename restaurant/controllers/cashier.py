from __future__ import print_function, unicode_literals

from datetime import datetime

from PyInquirer import prompt
from terminaltables import AsciiTable

from restaurant.core.bills import bills
from restaurant.core.orders import orders
from restaurant.utils.utils import color
from restaurant.utils.utils import get_questions


class RestaurantCashierCli:
    def __init__(self):
        self._questions = get_questions(1)

        self._service_number = 0
        self._orders = []

    def start(self):
        print("Hello, I hope you had a wonderful time.")
        question = self._questions["prompt_service_number"]
        answer = prompt(question)

        service_number = answer["service_number"]
        self._display_bill(service_number)
        self._process_payment(service_number)
        self._display_bill(service_number, True)
        self._exit()

    def _process_payment(self, service_number, charge=-1):
        question = self._questions["prompt_amount"]
        answer = prompt(question)

        if charge == -1:
            charge = orders.total_orders_value(service_number)

        paid_amount = int(answer["amount_paid"])

        if charge > paid_amount:
            print("Please input an amount that covers your bill!")
            self._process_payment(service_number, charge)

        date = datetime.today().strftime('%Y-%m-%d')

        bills.reset_table()
        bills.add_bill((service_number, charge, paid_amount, (paid_amount - charge), date))

    def _display_bill(self, service_number, paid=False):
        data = [
            ["Item", "Servings", " Unit Price", " Total Price"]
        ]
        for order in orders.get_orders(service_number):
            data.append(order)

        data.append(["", "", "", ""])
        print()

        if not paid:
            data.append(
                [f"{str(color.BOLD)}Total", "", "",
                 f"{str(orders.total_orders_value(service_number))} {str(color.END)}"])
            print("You made the following orders:")
        else:
            bill = bills.get_bill(service_number)
            data.append(
                [f"{str(color.BOLD)}S/N: {str(service_number)}", "", "",
                 f" {str(color.END)}"])
            date = str(bill["date"])
            data.append(
                [f"{str(color.BOLD)}DATE: {str(date)}", "", "", f" {str(color.END)}"])

            data.append(["", "", "", ""])
            data.append(
                [f"{str(color.BOLD)}Total", "", "",
                 f"{str(orders.total_orders_value(service_number))} {str(color.END)}"])
            paid = bill["paid"]
            data.append(
                [f"{str(color.BOLD)}Paid", "", "",
                 f"{str(paid)} {str(color.END)}"])
            balance = bill["balance"]
            data.append(
                [f"{str(color.BOLD)}Balance", "", "",
                 f"{str(balance)} {str(color.END)}"])
            print("Here is your receipt: ")

        table = AsciiTable(data)
        print()
        print(table.table)

    def _exit(self):
        print("Thank you for dining with us.")


cashier = RestaurantCashierCli()
