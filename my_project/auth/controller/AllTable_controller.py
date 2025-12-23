from flask import request
from ..service.all_table_service import AllTableService

all_table_service = AllTableService()

def calculate_stat_controller():
    """
    Контролер для обробки запиту на обчислення статистики через POST.
    :return: JSON відповідь з результатом або помилкою
    """
    try:
        # Отримуємо параметри з тіла запиту
        data = request.get_json()

        col_name = data.get('col_name')
        table_name = data.get('table_name')
        operation = data.get('operation')

        # Перевірка на наявність параметрів
        if not col_name or not table_name or not operation:
            return {"error": "Missing required parameters. col_name, table_name, and operation are required."}, 400

        # Перевірка на валідність параметрів операції
        valid_operations = ['AVG', 'SUM', 'COUNT']
        if operation not in valid_operations:
            return {"error": f"Invalid operation. Allowed values are {', '.join(valid_operations)}."}, 400

        # Викликаємо Service для обчислення статистики
        result = all_table_service.calculate_statistics(col_name, table_name, operation)
        return {"result": result}, 200

    except Exception as e:
        # Логування помилки
        print(f"Error: {str(e)}")
        return {"error": "An error occurred while processing your request"}, 500


def split_table_controller():
    """
    Контролер для запуску розбиття таблиці.
    :return: JSON відповідь з результатом або помилкою
    """
    try:
        all_table_service.split_tables()  # Викликаємо функцію з Service для розбиття таблиці
        return {"message": "Tables were split successfully."}, 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return {"error": "An error occurred during the split operation."}, 500