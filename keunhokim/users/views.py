import json
import bcrypt
import jwt

from django.http            import JsonResponse,HttpResponse
from django.core.exceptions import ValidationError
from utils                  import validate_email,validate_password

from django.views import View
from .models      import User,Coupon
from my_settings  import SECRET_KEY, algorithm

class UserSignUpView(View):
    def post(self,request):
        data = json.loads(request.body)

        try:
            name         = data.get('name',None)
            email        = data.get('email',None)
            password     = data.get('password', None)

            if User.objects.filter(email=email).exists():
                return HttpResponse(status=401)

            if not email or not password or not name:
                return JsonResponse({'message':'CHECK_INPUTS'},status=400)

            if validate_email(email) and validate_password(password):
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

                signup = User.objects.create(
                            name=name,
                            email=email,
                            password=hashed_password
                            )
                signup.coupon.add(Coupon.objects.get(id=2))

                return JsonResponse({'message': 'SIGN_UP_COMPLETE'}, status=201)

        except ValidationError as VE:
            return JsonResponse({'message': str(VE)},status=401)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class UserLoginView(View):
   def post(self,request):
       data = json.loads(request.body)

       try:
            email    = data['email']
            password = data['password']

            if not email or not password:
                return JsonResponse({'message':'CHECK_INPUTS'},status=400)

            if not User.objects.filter(email=email).exists():
                return HttpResponse(status=404)

            user = User.objects.get(email=email)

            if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                 access_token = jwt.encode({'user':user.id}, SECRET_KEY, algorithm)
                 return JsonResponse({'access_token':access_token}, status=200)
            else:
                return HttpResponse(status=403)

       except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
