import re
import json
import jwt
import bcrypt

from django.http import JsonResponse

from my_settings  import SECRET_KEY, ALGORITHM
from users.models import User

def password_validator(password):
    validator = re.compile('^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*_-])(\S){8,16}$')
    return validator.match(password)

def email_validator(email):
    validator = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$')
    return validator.match(email)
        
