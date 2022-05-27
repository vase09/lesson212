""" SELECT - ключевое слово для извлечения данных """
""" FROM - ключевое слово для определения таблицы """
"""" SELECT * FROM table_name - извлечение всей таблицы """
"""SELECT * (Используя '*', мы получим все данные из таблице"""
"""BETWEEN - для проверки между значениями, ( например WHERE _имя табл_ BETWEEN 1945 AND 1950 ) """
""" LIMIT ...OFFSET... ключевые слова для ограничения вывода данных"""
""" LIMIT - сколько строк вводим """
""" OFFSET - сколько строк пропустить перед выводом """
""" SELECT DISTINCT - получение значения без повторов , к примеру (SELECT DISTINCT 'location' FROM 'user')"""
""" SELECT (столбцы) from (таблица) WHERE (условие) - Получение данных с условием"""

##################################################################
import sqlite3

with sqlite3.connect("netflix.bd") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM netflix")

    for row in cursor.fetchall():  # """будет выводить на отдельную строку"""
        print(row)
#################################################
"""fetchall - получить все"""
"""fetchone - получить один результат"""
"""fetchmany - получить несколько результатов"""
#################################################

#Для более сложного запроса

with sqlite3.connect("netflix.bd") as connection:
    cursor = connection.cursor()
    """выносим запрос в переменную"""
    query = """
            SELECT * 
            FROM netflix
            WHERE director = 'Cristina Jacob'  #Получим данные с базы с данным именем
            
    """
    cursor.execute(query)


