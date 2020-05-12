
from django.core.exceptions import ValidationError


def first_name_validator(value):
    if value.startswith('v'):
        return value
    raise ValidationError
