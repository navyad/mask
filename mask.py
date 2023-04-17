from enum import Enum


class MaskType(Enum):
    EMAIL = "email"


class Email(object):

    @staticmethod
    def masker(user_part: str, chars_shown: int = 3) -> str:
        hidden_chars = len(user_part) - chars_shown
        return f'{user_part[:chars_shown]}{"*" * (hidden_chars)}'

    def mask(self, val) -> str:
        self.user_part, self.domain_part = val.rsplit('@')
        masked_usr = self.masker(self.user_part)
        return f'{masked_usr}@{self.domain_part}'


def factory(mask_type):
    masktypes = {"email": Email()}
    return masktypes[mask_type.value]


def mask(mask_type: MaskType, val: str) -> str:
    if not isinstance(mask_type, MaskType):
        raise Exception("Invalid masktype: expected MaskType")
    if not isinstance(val, str) or val == "":
        raise Exception("Invalid val: expected string")

    mask_instance = factory(mask_type)
    return mask_instance.mask(val)
