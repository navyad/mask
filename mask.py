from enum import Enum


class MaskType(Enum):
    EMAIL = "email"


def mask(mask_type: MaskType, val: str) -> str:
    if not isinstance(mask_type, MaskType):
        raise Exception("Invalid masktype: expected MaskType")
    if not isinstance(val, str) or val == "":
        raise Exception("Invalid val: expected string")
