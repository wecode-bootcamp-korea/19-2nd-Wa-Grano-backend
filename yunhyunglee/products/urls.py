from django.urls import path
from .views      import CategoryView, DestinationView, ProductDetailView

urlpatterns = [
        path('/category', CategoryView.as_view()),
        path('/destination/<int:category_id>', DestinationView.as_view()),
        path('/destination', DestinationView.as_view()),
        path('/productdetail/<int:product_id>', ProductDetailView.as_view()),
        ]
