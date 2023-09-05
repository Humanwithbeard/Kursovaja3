from src.utils import format_date


def test_format_date():
    assert format_date("2019-08-26T10:50:58.294041") == "26-08-2019"
    assert format_date("2018-07-11T02:26:18.671407") == "11-07-2018"
