import sqlite3 as sql

from data import USERS
from database_controller import QUERY_FILL_DATA, QUERY_SELECT_OLDER_30

DB_PATH = "task_2.db"


def fill_database():
    with sql.connect(DB_PATH) as conn:
        for user in USERS:
            conn.cursor().execute(QUERY_FILL_DATA,(user))
        return "Данные сохранены"


def select_older_30():
    with sql.connect(DB_PATH) as conn:
        selected_users = []
        result = conn.cursor().execute(QUERY_SELECT_OLDER_30,).fetchall()
        for row in result:
            selected_users.append(row)
        return selected_users


print(fill_database())
print(select_older_30())
