from src.utils import mask_card_number


def test_mask_card_number():
    assert mask_card_number("Счет 38611439522855669794") == "Счет 3861 14** **** 9794"
    assert mask_card_number("") == "Нет данных"
    assert mask_card_number("Visa Classic 4195191172583802") == "Visa Classic 4195 19** **** 3802"
