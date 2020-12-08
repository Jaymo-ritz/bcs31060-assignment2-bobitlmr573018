from restaurant.core.database import database as db
from restaurant.utils.setup import setup_example_db


def test_execute_command():
    insert_name = "John Doe"
    command = "INSERT INTO patron(name, table_number) VALUES(?,?)"
    row_id = db.execute_command(command, (insert_name, 12))
    query = "SELECT name FROM patron WHERE service_number=?"
    row = db.execute_command(query, (row_id,))

    select_name = row[0]["name"]
    assert insert_name == select_name


def test_create_connection():
    connection = db._create_connection()
    assert connection is not None
    connection.close()


if __name__ == '__main__':
    setup_example_db()
