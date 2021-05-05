from django.urls import path
from .views import ProductDetailCategory, ProductRestaurant
  
urlpatterns = [
        path('/destination/<int:destination_id>', ProductDetailCategory.as_view()),
        path('/restaurant', ProductRestaurant.as_view())
#        path('/products', ProductsView.as_view())
        ]
