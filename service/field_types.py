from enum import Enum


class FieldTypes(str, Enum):
    text = "text"
    email = "email"
    date = "date"
    phone = "phone"
