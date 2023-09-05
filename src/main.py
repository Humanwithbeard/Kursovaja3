import json
from src.utils import process_executed_operations, print_last_five_operations


def main():
    """
    Основная функция. Извлекает инфу из файла operations.json и собственно, выдает результат
    """
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    last_five_operations = process_executed_operations(data)
    print_last_five_operations(last_five_operations)


if __name__ == "__main__":
    main()

