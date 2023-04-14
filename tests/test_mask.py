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
