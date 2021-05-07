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
        if not category_id or not Category.objects.get(id=category_id).exists():
            return JsonResponse({'message':'BAD_REQUEST'}, status=400)

        data = [{
            'name': destination.name,
            'image_url': destination.image_url
        } for destination in Category.objects.get(id=category_id).destination.all()]

        return JsonResponse({'data':data},status=200)

class ProductView(View):
    def get(self,request,category_id):
        destinations = Category.objects.get(id=category_id).destination.all()

        data = [{
            'name': destination.name,
            'image_url': destination.image_url
            } for destination in destinations]

        return JsonResponse({'data':data},status=200)

class ProductDetailView(View):
    def get(self,request):
        is_room     = request.GET.get('is_room', None)
        is_dinning  = request.GET.get('is_dinning', None)

        if is_dinning == 1:

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

class RoomDetailView(View):
    def get(self,request):































