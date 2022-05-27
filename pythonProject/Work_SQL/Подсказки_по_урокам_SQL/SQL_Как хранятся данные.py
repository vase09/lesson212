"""
Фильтрация
Информация по детским фильмам (G) за последние пать лет,
у которых проставлена дата добавления
"""
"""
Написание разных типов данных в SQL
1. Числовые - 1 2 3 4
2. Текс - 'text'
3. Даты - '20-01-01 00:00:00'
4. NULL
"""
import sqlite3

with sqlite3.connect("netflix.bd") as connection:
    cursor = connection.cursor()
    """выносим запрос в переменную"""
    query = """
            SELECT title, release_year
            FROM netflix
            WHERE rating = 'G'
            AND release_year > 2016
            AND date_added IS NOT NULL
    """