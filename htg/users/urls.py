from django.urls import path

from .views import SignInView 

urlpatterns = [
  #  path('/sign-up', SignupView.as_view()),
    path('/sign-in', SignInView.as_view()),
    ]
