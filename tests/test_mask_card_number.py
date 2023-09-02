import json
import pytest
from src.main import mask_card_number


@pytest.fixture
def json_data():
    with open('operations.json', 'r') as file:
        data = json.load(file)
    return data


def test_mask_card_number():
    assert mask_card_number("38611439522855669794") == "3 8611** **** 9794"
