from django.urls import path

from .views import SignInView, UserView

urlpatterns = [
        path('/users', UserView.as_view()),
        path('/signin', SignInView.as_view())
        ]
