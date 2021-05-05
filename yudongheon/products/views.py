from django.views import View
from django.http  import JsonResponse, HttpResponse

from .models import *

class ProductDetailCategory(View):
    def get(self, request, destination_id = None):

        if not destination_id or not Destination.objects.filter(id=destination_id).exists():
            return JsonResponse({'error':'BAD_REQUEST'}, status=404)

        detail_category = [i.name for i in Destination.objects.get(id=destination_id).category_set.all()]

        return JsonResponse({'data' : detail_category}, status=200)

class ProductRestaurant(View):
    def get(self, request):
        
        try:
            restaurant = [
                    {
                        'name'   : restaurant.name,
                        'rating' : restaurant.rating,
                        'price'  : restaurant.price
                        } for restaurant in Product.objects.order_by('?').filter(is_dinning=1)[:5]
                    ]
            return JsonResponse({'data' : restaurant}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'key_error'}, status=400)
