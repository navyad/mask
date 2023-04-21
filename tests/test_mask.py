import pytest
from mask import mask, MaskType


def test_invalid_mask_type():
    with pytest.raises(Exception) as exc_info:
        mask(1, "abc")
    assert exc_info.value.args[0] == "Invalid masktype: expected MaskType"


def test_invalid_val():
    with pytest.raises(Exception) as exc_info:
        mask(MaskType.EMAIL, 111)
    assert exc_info.value.args[0] == "Invalid val: expected string"


def test_email_mask():
    masked = mask(MaskType.EMAIL, "reliko9368@lieboe.com")
    assert masked == "rel*******@lieboe.com"


def test_invalid_email():
    with pytest.raises(Exception) as exc_info:
        mask(MaskType.EMAIL, "reliko9368lieboe.com")
    assert exc_info.value.args[0] == "Invalid email"


def test_password():
    password = "thisisdummypwd"
    expected = "*" * len(password)
    masked = mask(MaskType.PASSWORD, password)
    assert masked == expected


def test_mobile():
    expected = "446***899"
    masked = mask(MaskType.MOBILE, "446681899")
    assert masked == expected
