import unittest.mock as mock
from src.utils import load_data_from_json


def test_load_data_from_json():
    with mock.patch('builtins.open', mock.mock_open(read_data='[{"data": "value"}]')):
        data = load_data_from_json()
    assert data == [{"data": "value"}]
