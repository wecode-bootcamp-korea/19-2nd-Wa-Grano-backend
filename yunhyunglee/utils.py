import re
import jwt
import json

from django.http  import JsonResponse

from my_settings  import SECRET_KEY
from users.models import User


def VALIDATOR_EMAIL(email):
    validator = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    if validator.match(email):
        return True
    return False

def VALIDATOR_PASSWORD(password):
    validator = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')

    if validator.match(password):
        return True
    return False


def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
            user         = User.objects.get(id=payload['user'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper
