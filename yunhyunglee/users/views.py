import json
import bcrypt
import jwt
import re

from django.views import View
from django.http  import JsonResponse, HttpResponse

from my_settings  import SECRET_KEY
from .models      import User
from utils        import EMAIL_VALIDATOR, PASSWORD_VALIDATOR


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        name     = data.get('name', None)
        email    = data.get('email', None)
        password = data.get('password', None)

        if not name or not email or not password:
            return JsonResponse({'message' : 'CHECK_YOUR_INPUT'}, status=400)

        if not EMAIL_VALIDATOR(email):
            return JsonResponse({'message' : 'INVALID_EMAIL'}, status=400)

        if not PASSWORD_VALIDATOR(password):
            return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message' : 'EMAIL_EXIST'}, status=409)

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        User.objects.create(
                name     = name,
                email    = email,
                password = hashed_password
                )

        return HttpResponse(status=201)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        email    = data.get('email', None)
        password = data.get('password', None)

        if not email or not password:
            return JsonResponse({'message' : 'CHECK_YOUR_INPUT'}, status=400)

        if not User.objects.filter(email=email).exists():
            return HttpResponse(status=401)

        user = User.objects.get(email=email)

        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            access_token = jwt.encode({'user':user.id}, SECRET_KEY, algorithm='HS256')
            return JsonResponse({'access_token' : access_token}, status=200)

        return HttpResponse(status=401)
