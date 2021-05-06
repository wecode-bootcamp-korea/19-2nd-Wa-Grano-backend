import bcrypt
import jwt
import json

from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import User #UserCoupon, Coupon

from my_settings import password_validation, email_validation, algorithm

PASSWORD_LENGTH = 8

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        email           = data.get('email', None)
        password        = data.get('password', None)
        check_password  = data.get('check_password', None)
        name            = data.get('name', None)
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        if not email or not password or not check_password or not name:
            return JsonResponse({'message' : 'CHECK_YOUR_INPUT'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message' : 'EXITST_EMAIL'}, status=400)

        if not password_validation.match(password):
            return JsonResponse({'message' : 'NOT_MATCH_PASSWORD_FORM'}, status=400)

        if not password == check_password:
            return JsonResponse({'message' : 'CHECK_YOUR_INPUT_PASSWORD'})
        
        if not email_validation.match(email):
            return JsonResponse({'message' : 'NOT_MATCHED_EMAIL_FORM'}, status=400)

        User.objects.create(
                email           = email,
                password        = hashed_password,
                name            = name,
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
                access_token = jwt.encode({'id':'user_email_id'}, 'SECRET_KEY', algorithm)
                return JsonResponse({'access_token' : access_token}, status=200)
            
            return JsonResponse({'message' : 'NOT_MACTHED_PASSWORD'}, status=401)

        return JsonResponse({'message' : 'NOT_MACTHED_EMAIL'}, status=401)

