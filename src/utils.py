from datetime import datetime
import json


def load_data_from_json():
    """
    Извлекает инфу из файла operations.json
    """
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def mask_card_number(card_number):
    """
    Маскировка кода карточки (цифры в звездочки)
    """
    digits = ''.join(char for char in card_number if char.isdigit())
    if len(digits) >= 16:
        masked_number = digits[:4] + ' ' + digits[4:6] + '** **** ' + digits[-4:]
    else:
        masked_number = "Нет данных"
    return masked_number


def mask_account_number(account_number):
    """
    Маскировка номера счета (цифры в звездочки)
    """
    masked_number = '**' + account_number[-6:-4] + ' ' + account_number[-4:]
    return masked_number


def format_date(date_str):
    """
    Форматировка даты по нужный стандарт
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d-%m-%Y")


def process_executed_operations(data):
    """
    Обработка списка и вывод только выполненых операций.
    Так же сортировка даты
    """
    executed_operations = sorted(
        (operation for operation in data if operation.get('state') == 'EXECUTED'),
        key=lambda operation: operation['date'],
        reverse=True
    )
    return executed_operations[:5]


def print_last_five_operations(last_five_operations):
    """
    Вывод
    """
    for operation in last_five_operations:
        date = format_date(operation['date'])
        description = operation['description']
        from_account = mask_card_number(operation.get('from', operation.get('fromAccount', '')))
        to_account = mask_account_number(operation.get('to', operation.get('toAccount', '')))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        print(f'{date} {description}')
        print(f'{from_account} -> {to_account}')
        print(f'{amount} {currency}\n')
