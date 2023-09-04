import json


def mask_card_number(card_number):
    dig_l = []
    char_l = []
    empty_l = []
    for char in card_number:
        if char.isdigit():
            char_l.append(char)
        else:
            dig_l.append(char)
    if char_l:
        new_new = ''.join(dig_l) + ''.join(char_l)[:4] + ' ' + ''.join(char_l)[4:6] + '** **** ' + ''.join(char_l)[
-4:] + ''.join(
            empty_l)
    else:
        new_new = "Нет данных"
    return new_new


def mask_account_number(account_number):
    masked_number = '**' + account_number[-6:-4] + ' ' + account_number[-4:]
    return masked_number


def last_five_exe():
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    executed_operations = sorted(
        (operation for operation in data if operation.get('state') == 'EXECUTED'),
        key=lambda operation: operation['date'],
        reverse=True
    )
    last_five_operations = executed_operations[:5]

    for operation in last_five_operations:
        date = operation['date'].split('T')[0]
        description = operation['description']
        from_account = mask_card_number(operation.get('from', operation.get('fromAccount', '')))
        to_account = mask_account_number(operation.get('to', operation.get('toAccount', '')))
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        print(f'{date} {description}')
        print(f'{from_account} -> {to_account}')
        print(f'{amount} {currency}\n')


last_five_exe()
