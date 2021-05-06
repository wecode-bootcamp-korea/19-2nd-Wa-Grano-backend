from django.urls import path

from .views import Popular_Destinations,DinningView

urlpatterns =[

        path('/products', Popular_Destinations.as_view()),
        path('/dinning/<int:product_id>', DinningView.as_view())



        ]
