from src.utils import process_executed_operations
import pytest


@pytest.fixture
def sample_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2222-22-22",
        },
        {
            "state": "PENDING",
            "date": "2222-22-22",
        },
    ]


def test_process_executed_operations(sample_data):
    result = process_executed_operations(sample_data)
    for operation in result:
        assert operation["state"] == "EXECUTED"