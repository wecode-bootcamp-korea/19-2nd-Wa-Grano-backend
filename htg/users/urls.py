from django.urls import path

from .views import SignInView, SignupView

urlpatterns = [
    path('/sign-up', SignupView.as_view()),
    path('/sign-in', SignInView.as_view()),



        ]
