from django.views import View
from .models      import *
from django.http  import HttpResponse,JsonResponse

class CategoryView(View):
    def get(self, request):
       categories = Category.objects.all()

       data = [{
           'name'     : category.name,
           'image_url': category.image_url
       } for category in categories]

       return JsonResponse({'data':data},status=200)

class DestinationView(View):
    def get(self,request,category_id):
        destinations = Category.objects.get(id=category_id).destination.all()

        data = [{
            'name': destination.name,
            'image_url': destination.image_url
            } for destination in destinations]

        return JsonResponse({'data':data},status=200)

class DinningView(View):
    def get(self,request,is_dinning):
        restaurants = Product.objects.filter(is_dinning=1)

        data = [{
            'name'          : restaurant.name,
            'rating'        : restaurant.rating,
            'description'   : restaurant.description,
            'address'       : restaurant.address,
            'latitude'      : restaurant.latitude,
            'longitude'     : restaurant.longitude,
            'category'      : restaurant.category.name,
            'destination'   : restaurant.destination.name,
            'district'      : restaurant.district.name,
            'price'         : restaurant.price,
            'dinning_type'  : Dinning.objects.get(id=restaurant.dinning_id).dinning_type.name,
            'dinning_option': Dinning.objects.get(id=restaurant.dinning_id).food_type.name,

            } for restaurant in restaurants]

        return JsonResponse({'data':data},status=200)

class RoomView(View):
    def get(self,request):





























