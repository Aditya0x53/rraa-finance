import re
from typing import Tuple


def validate_phone(phone: str) -> bool:
    phone = str(phone).strip()
    pattern = r'^[0-9]{10}$'
    return bool(re.match(pattern, phone))


def validate_name(name: str) -> bool:
    name = str(name).strip()
    if not name or len(name) < 2:
        return False
    return name.replace(" ", "").isalpha()


def validate_amount(amount) -> Tuple[bool, str]:
    try:
        amount_float = float(amount)
        if amount_float < 0:
            return False, "Amount cannot be negative"
        if amount_float == 0:
            return False, "Amount must be greater than zero"
        return True, ""
    except ValueError:
        return False, "Invalid amount format"


def validate_dlno(dlno: str) -> bool:
    dlno = str(dlno).strip()
    pattern = r'^DL\d{6}$'
    return bool(re.match(pattern, dlno))