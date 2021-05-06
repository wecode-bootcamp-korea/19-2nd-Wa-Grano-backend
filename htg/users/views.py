import json
import bcrypt
import jwt
import re

from django.views import View
from django.http import JsonResponse, HttpResponse

from my_settings  import SECRET_KEY, ALGORITHM
from .models import User

class SignInView(View):
    def post(self, request):

        data = json.loads(request.body)
        
        email    = data.get('email',None)
        password = data.get('password',None)

        if not User.objects.filter(email=email).exists:
            return JsonResponse({'message':'NOT EXISTS EMAIL'})
            
        user            = User.objects.get(email=email)
        hashed_password = user.password.encode('utf-8')

        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return JsonResponse({'message':'INVALID_USER'},status=401)
            
        access_token = jwt.encode({'user_id':user.id}, SECRET_KEY, ALGORITHM)
        
        return JsonResponse({'message':'GIVE A ACCESS_TOKEN FOR YOU'},status=200)
