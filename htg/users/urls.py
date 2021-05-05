from django.urls import path

from .views import SignupView

urlpatterns = [
    path('/sign-up', SignupView.as_view()),



        ]
