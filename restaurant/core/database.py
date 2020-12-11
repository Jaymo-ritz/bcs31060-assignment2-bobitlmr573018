import os
import os.path as path
import sqlite3
from sqlite3 import Error

from restaurant.utils.utils import get_root_dir


class RestaurantDatabase:
    def __init__(self):
        self.table = None
        self._database = path.join(get_root_dir(), "database", "restaurant.db")

    def _create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self._database)
        except Error as e:
            raise e
        finally:
            if connection:
                return connection

    def execute_command(self, command, values=()):
        connection = self._create_connection()
        connection.row_factory = sqlite3.Row

        try:
            cursor = connection.cursor()
            if len(values):
                cursor.execute(command, values)
            else:
                cursor.execute(command)

            if cursor.lastrowid:
                results = cursor.lastrowid
            else:
                results = cursor.fetchall()

        except Error as e:
            raise e
        finally:
            connection.close()

        return results

    def execute_script(self, script):
        connection = self._create_connection()
        try:
            cursor = connection.cursor()
            cursor.executescript(script)
            connection.commit()
        except Error as e:
            raise e
        finally:
            connection.close()

    def create_database(self):
        sql_file = path.join(get_root_dir(), "database", "database.sql")
        fd = open(sql_file, 'r')
        commands = fd.read()
        fd.close()
        self.execute_script(commands)

    def reset_database(self):
        if os.path.isfile(self._database):
            os.remove(self._database)

        self.create_database()

    def reset_table(self):
        command = "DELETE FROM " + self.table
        self.execute_command(command)

    def database_exists(self):
        return os.path.isfile(self._database)


database = RestaurantDatabase()
