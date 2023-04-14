
import pytest
from mask import mask, MaskType


def test_invalid_mask_type():
    with pytest.raises(Exception) as exc_info:
        mask(1, "abc")

def test_invalid_val():
    with pytest.raises(Exception) as exc_info:
        mask(MaskType.EMAIL, "abc")
