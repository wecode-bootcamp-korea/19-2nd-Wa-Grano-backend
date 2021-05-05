import re
import bcrypt
import jwt
import json

from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import User #UserCoupon, Coupon

PASSWORD_LENGTH = 8

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)
        name = data.get('name', None)
        last_name = data.get('last_name', None)
        first_name = data.get('first_name', None)
        phone_number = data.get('phone_number', None)
        
        password_validation = re.compile('^[a-zA-Z0-9]*$')
        email_validation    = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        
        hashed_password     = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        if not email or not password or not name or not last_name or not first_name or not phone_number:
            return JsonResponse({'message' : 'CHECK_YOUR_INPUT'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message' : 'EXITST_EMAIL'}, status=400)

        if not password_validation.match(password):
            return JsonResponse({'message' : 'NOT_MATCH_PASSWORD_FORM'}, status=400)
        
        if not email_validation.match(email):
            return JsonResponse({'message' : 'NOT_MATCHED_EMAIL_FORM'}, status=400)

        User.objects.create(
                email           = email,
                password        = hashed_password,
                name            = name,
                last_name       = last_name,
                first_name      = first_name,
                phone_number    = phone_number,
                )

        return HttpResponse(status=200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        email = data.get('email', None)
        password = data.get('password', None)

        if not email or not password:
            return JsonResponse({'error' : 'CHECK_YOUR_INPUT'}, status=401)

        if User.objects.filter(email=email).exists():
            user_email = User.objects.get(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user_email.password.encode('utf-8')):
                access_token = jwt.encode({'id':'user_email_id'}, 'SECRET_KEY', algorithm='HS256')
                return JsonResponse({'access_token' : access_token}, status=200)
            
            return JsonResponse({'message' : 'NOT_MACTHED_PASSWORD'}, status=401)

        return JsonResponse({'message' : 'NOT_MACTHED_EMAIL'}, status=401)
