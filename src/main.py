from src.utils import process_executed_operations, print_last_five_operations, load_data_from_json


def main():
    """
    Основная функция. Выдает результат
    """
    data = load_data_from_json()

    last_five_operations = process_executed_operations(data)
    print_last_five_operations(last_five_operations)


if __name__ == "__main__":
    main()

