import json
from src.main import mask_card_number


def json_data():
    with open('operations.json', 'r') as file:
        data = json.load(file)
    return data


def test_mask_card_number():
    assert mask_card_number("Счет 38611439522855669794") == "Счет 3861 14** **** 9794"