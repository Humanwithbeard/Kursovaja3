from src.utils import mask_account_number


def test_mask_account_number():
    assert mask_account_number("77613226829885488381") == "**48 8381"
    assert mask_account_number("43241152692663622869") == "**62 2869"
