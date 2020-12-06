import argparse

from restaurant.controllers.cashier import cashier
from restaurant.controllers.waiter import waiter
from restaurant.core.database import database
from restaurant.utils.setup import setup_example_db


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--waiter", help="run the program in waiter mode.", action="store_true")
    parser.add_argument("-c", "--cashier", help="run the program in cashier mode.", action="store_true")
    parser.add_argument("-r", "--reset", help="reset the database", action="store_true")

    args = parser.parse_args()
    if not database.database_exists() or args.reset:
        print("Creating database and populating it with test data")
        database.reset_database()
        setup_example_db()  # TODO: replace with something concrete

    if args.cashier:
        cashier.start()
    elif args.waiter:
        waiter.start()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
