import re
from django.core.exceptions import ValidationError

def validate_email(value):
    email_reg = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    regex = re.compile(email_reg)
    if not regex.match(value):
       raise ValidationError('INVALID_EMAIL')
    else:
        return value

def validate_password(value):
    password_reg = r"(^(?=.*[a-zA-Z])((?=.*\d)|(?=.*\W)).{6,20}$)"
    regex = re.compile(password_reg)

    if not regex.match(value):
        raise ValidationError('INVALID_PASSWORD')

    else:
        return value
