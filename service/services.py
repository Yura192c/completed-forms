from datetime import datetime
import re


def is_valid_date(date_str):
    formats = ['%d.%m.%Y', '%Y-%m-%d']

    for fmt in formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            pass


def is_valid_phone_number(phone_str):
    # Определение паттерна для номера телефона "+7 xxx xxx xx xx"
    pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    return bool(pattern.match(phone_str))


def get_field_type(value):
    if is_valid_date(value):
        return "date"

    elif is_valid_phone_number(value):
        return "phone"

    elif '@' in value and '.' in value.split('@')[1]:
        return "email"

    else:
        return "text"
