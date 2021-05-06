import json
import bcrypt
import jwt
import re

from django.views import View
from django.http  import JsonResponse, HttpResponse

from my_settings  import SECRET_KEY, ALGORITHM
from .models import User


class SignupView(View):
    def post(self, request):

        data = json.loads(request.body)
        MINIMUM_PASSWORD_LENGTH = 8

        email    = data.get('email',None)
        password = data.get('password',None)
        name     = data.get('name',None)

        email_check = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email_check = email_check.match(email)

             
        if not email_check:
            return JsonResponse({'message' : 'INVALID EMAIL'}, status=400)

        if len(password) < MINIMUM_PASSWORD_LENGTH:
            return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'}, status = 400)

        if User.objects.filter(email = email).exists():
            return JsonResponse({'message':'EMAIL ALREADY EXISTS'},status=400)
            
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode()

        User.objects.create(
            email    = email, 
            password = hashed_password,
            name     = name,
            )
        
        return JsonResponse({'message' : 'SUCCESS'}, status=201)


                    

                 
        


        
        
