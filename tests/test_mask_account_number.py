from src.utils import mask_account_number


def test_mask_account_number():
    assert mask_account_number("77613226829885488381") == "**48 8381"
