""" Подключение к SQLite 3 """

import sqlite3

"""Подключение к базе данных"""

connection = sqlite3.connect("указываем базу данных")

cursor = connection.cursor()
cursor.execute("""Здесь будут наши команды""")

"""Закрытие соединения с базой данных"""
connection.close()

"""Упрощенный вариант"""

with sqlite3.connect("указываем базу данных") as connection:
    cursor = connection.cursor()
    cursor.execute("""Здесь будут наши команды""")
