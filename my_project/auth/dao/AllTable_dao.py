from sqlalchemy import text
from models import db
import mysql.connector
from mysql.connector import Error

def split_table():
    """
    Розбиває таблицю 'sensors' на кілька таблиць з унікальними іменами.
    Записує події в 'event_log'.
    """
    try:
        # Підключення до бази даних
        conn = mysql.connector.connect(user='your_user', password='your_password', host='localhost', database='your_database')
        cursor = conn.cursor()

        # Отримуємо список idSensor з таблиці sensors
        cursor.execute("SELECT idSensor FROM sensors")
        sensors = cursor.fetchall()

        for sensor in sensors:
            row_id = sensor[0]
            table_suffix = f"split_{int(time.time())}_{row_id}"  # Унікальне ім'я для кожної таблиці
            # Створюємо нову таблицю, подібну до sensors
            create_query = f"CREATE TABLE {table_suffix} LIKE sensors"
            cursor.execute(create_query)

            # Логування в таблицю event_log
            log_query = f"""
            INSERT INTO event_log (event_time, event_type, description, Users_idUser, Sensors_idSensor)
            VALUES (NOW(), 'Split Operation', 'Created table {table_suffix}', 1, {row_id})
            """
            cursor.execute(log_query)

        # Підтверджуємо зміни
        conn.commit()

        cursor.close()
        conn.close()

    except Error as err:
        print(f"Error: {err}")
        raise Exception("An error occurred while executing the split_table procedure.")

def calculate_stat(col_name, table_name, operation):
    """
    Функція для обчислення статистики на основі запиту.
    :param col_name: Назва колонки
    :param table_name: Назва таблиці
    :param operation: Операція для обчислення (AVG, SUM, COUNT)
    :return: Результат обчислення
    """
    try:
        # Підключення до бази даних
        conn = mysql.connector.connect(user='your_user', password='your_password', host='localhost', database='your_database')
        cursor = conn.cursor()

        # Формуємо динамічний SQL запит
        query = f"SELECT {operation}({col_name}) FROM {table_name}"

        # Логування запиту для діагностики
        print(f"Executing query: {query}")

        cursor.execute(query)
        result = cursor.fetchone()

        # Закриваємо з'єднання
        cursor.close()
        conn.close()

        if result:
            return result[0]  # Повертаємо перше значення з результату
        else:
            raise ValueError("No data found for the given query")

    except mysql.connector.Error as err:
        # Логування помилки бази даних
        print(f"Database error: {str(err)}")
        raise Exception("Database error occurred")

    except Exception as e:
        # Логування помилки
        print(f"Error: {str(e)}")
        raise