from __future__ import print_function, unicode_literals

import random
from itertools import permutations

from PyInquirer import prompt
from terminaltables import AsciiTable

from restaurant.core.meals import meals
from restaurant.core.menu import menu
from restaurant.core.orders import orders
from restaurant.core.patron import patron
from restaurant.utils.utils import get_questions
from restaurant.utils.utils import color


class RestaurantWaiterCli:
    def __init__(self):
        self.questions = get_questions(0)

        self._service_number = 0
        self._orders = []

    def _serve(self):
        self._welcome_patron()
        self._order_item()
        self._confirm_orders()
        self._set_serving_order()
        self._commit_orders()
        self._exit(True)

    def _welcome_patron(self):
        print("Welcome to our restaurant!")
        self._request_patron_name()

    def _request_patron_name(self):
        question = self.questions["prompt_name"]
        answer = prompt(question)
        table_number = random.randint(1, 12)
        service_number = patron.new_patron((answer["patron_name"], table_number))
        self._service_number = service_number

    def _order_item(self):
        while True:
            item_type = self._select_menu()

            question = self.questions["prompt_item"]
            items = menu.get_items(item_type)
            question['choices'] = []
            for item in items:
                question['choices'].append(item["name"])

            answer = prompt(question)
            item = answer["item_ordered"]

            question = self.questions["prompt_servings"]
            answer = prompt(question)
            servings = answer["servings_count"]

            self._add_to_orders([item, servings])

            question = self.questions["prompt_add_order"]
            answer = prompt(question)
            if not answer["add_order"]:
                break

    def _select_menu(self):
        question = self.questions["prompt_menu"]
        item_types = menu.get_item_types()
        question["choices"] = []
        for item_type in item_types:
            question['choices'].append(item_type["name"])

        answer = prompt(question)
        return answer["selected_menu"]

    def _confirm_orders(self):
        while True:
            print("You have made the following orders:")
            self._print_orders()
            question = self.questions["prompt_confirm_orders"]
            answer = prompt(question)
            if answer["change_order"]:
                question = self.questions["prompt_order_changes"]
                change_type = prompt(question)["order_change_type"]

                if change_type == question["choices"][0]:
                    self._order_item()
                elif change_type == question["choices"][1]:
                    self._update_order()
                else:
                    self._remove_order()
            else:
                break

    def _update_order(self):
        question = self.questions["get_update_order"]
        question["choices"] = []

        for order in self._orders:
            question["choices"].append(order[0])

        answer = prompt(question)
        order_to_update = answer["order_to_update"]
        question = self.questions["get_updated_servings"]
        answer = prompt(question)
        servings = answer["servings_count"]

        self._remove_from_order(order_to_update)
        self._add_to_orders((order_to_update, servings))

    def _remove_order(self):
        question = self.questions["get_delete_order"]
        question["choices"] = []

        for order in self._orders:
            question["choices"].append(order[0])

        answer = prompt(question)
        order_to_delete = answer["order_to_delete"]

        self._remove_from_order(order_to_delete)

    def _set_serving_order(self):
        order_types = []
        for order in self._orders:
            order_types.append(meals.get_meal_type(order[0]))

        order_types = list(set(order_types))

        possible_orders = list(permutations(order_types))

        question = self.questions["prompt_serving_order"]
        question["choices"] = []

        if len(order_types) > 1:

            for serving_order in possible_orders:
                question["choices"].append(", ".join(list(serving_order)))

            answer = prompt(question)

            print("You will be served in the following order: ", answer["serving_order"])

    def _commit_orders(self):
        for order in self._orders:
            orders.add_order((self._service_number, order[0], order[1]))

    def _add_to_orders(self, item):
        for order in self._orders:
            if order[0] == item[0]:
                self._remove_from_order(order)
                order = list(order)
                order[1] = int(order[1]) + int(item[1])
                item = tuple(order)

        self._orders.append(item)

    def _remove_from_order(self, item):
        for order in self._orders:
            if order[0] == item[0]:
                self._orders.remove(order)

    def _print_orders(self):
        data = [
            ["Item", "Servings"]
        ]
        for order in self._orders:
            data.append(order)

        table = AsciiTable(data)
        print(table.table)

    def _exit(self, placed_order=False):
        if placed_order:
            print("Your orders have been successfully placed.")
            print(
                f"Your {str(color.BOLD)} {str(color.YELLOW)} Service number is {str(self._service_number)} "
                f"{str(color.END)},"
                f" The Cashier will require it to process your bill")

        print("Have a wonderful day!")

    def start(self):
        self._serve()


waiter = RestaurantWaiterCli()
