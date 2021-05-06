import re
import jwt
import my_settings

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from users.models                import User


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


def login_required(func):
    def decorator(self, request, *args, **kwargs):
        try:
            encoded_token = request.headers['Authorization']
            decoded_token = jwt.decode(encoded_token, my_settings.SECRET_KEY, algorithms=my_settings.algorithm)
            user = User.objects.get(id=decoded_token['user'])
            request.user = user
            return func(self, request, *args, **kwargs)
        except User.DoesNotExist:
            return JsonResponse({"message": "UNKNOWN_USER"}, status=401)
        except KeyError:
            return JsonResponse({"message": "INVALID_LOGIN"}, status=401)
        except jwt.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=401)

    return decorator
