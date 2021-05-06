from django.urls import path
from .views import UserSignUpView,UserLoginView

urlpatterns = [
    path('/signup', UserSignUpView.as_view()),
    path('/login', UserLoginView.as_view()),
]