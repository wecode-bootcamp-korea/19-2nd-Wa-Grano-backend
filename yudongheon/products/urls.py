from django.urls import path
from .views import BestSeller, Destination, BestSeller

urlpatterns = [
        path('/destinations', Destination.as_view()),
        path('/bestseller', BestSeller.as_view())
        ]
