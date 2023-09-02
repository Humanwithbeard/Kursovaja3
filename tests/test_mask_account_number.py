import json
import pytest
from src.main import mask_account_number

@pytest.fixture
def json_data():
    with open('operations.json', 'r') as file:
        data = json.load(file)
    return data


def test_mask_account_number():
    assert mask_account_number("77613226829885488381") == "**48 8381"

