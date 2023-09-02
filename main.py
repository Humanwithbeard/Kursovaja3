import json


def last_five_exe():
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    executed_operations = sorted(
        (operation for operation in data if operation.get('state') == 'EXECUTED'),
        key=lambda operation: operation['date'],
        reverse=True
    )
    last_five_operations = executed_operations[:5]

    def mask_card_number(card_number):
        masked_number = card_number[:6] + ' ' + card_number[6:10] + '** **** ' + card_number[-4:]
        return masked_number

    def mask_account_number(account_number):
        masked_number = '**' + account_number[-6:-4] + ' ' + account_number[-4:]
        return masked_number

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

