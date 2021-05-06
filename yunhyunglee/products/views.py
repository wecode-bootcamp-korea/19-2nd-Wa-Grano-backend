from django.views import View
from django.http  import JsonResponse, HttpResponse

from .models          import Category, Product


class CategoryView(View):
    def get(self, request):
        
        data = [{
            'name'      : category.name,
            'image_url' : category.image_url
            } for category in Category.objects.all()]

        return JsonResponse({'data' : data}, status=200)


class DestinationView(View):
    def get(self, request, category_id=1):

        if not category_id or not Category.objects.filter(id=category_id).exists():
            return JsonResponse({'message' : 'BAD_REQUEST'}, status=400)

        data = [{
            'name'      : destination.name,
            'image_url' : destination.image_url
           } for destination in Category.objects.get(id=category_id).destination.all()]

        return JsonResponse({'data' : data}, status=200)


class ProductDetailView(View):
    def get(self, request, product_id=None):

        if not product_id or not Product.objects.filter(id=product_id):
            return JsonResponse({'message' : 'BAD_REQUEST'}, status=400)

        product = Product.objects.get(id=product_id)

        product_list = []

        product_list.append({
                'name' : product.name,
                'rating' : product.rating,
                'description' : product.description,
                'address' : product.address,
                'latitude' : product.latitude,
                'longitude' : product.longitude,
                'city'      : product.city.name,
                'district' : product.district.name,
                'price' : product.price,
                'is_room' : product.is_room,
                'is_dinning' : product.is_dinning,
                'image' : [{
                    'image_url' : image.image_url
                    } for image in product.productimage_set.all()],
                })

        if Product.objects.filter(id=product_id, is_room=True):
            room = {
                    'room_type'   : product.room.room_type.name,
                    'star_rating' : product.room.star_rating,
                    'convenience' : [{
                        'name'         : convenience.name,
                        'service_type' : convenience.service_type.name
                        } for convenience in product.room.convenience.all()]
                    }

            product_list.append(room)

            return JsonResponse({'message' : product_list}, status=200)

        if Product.objects.filter(id=product_id, is_dinning=True):
            dinning = {
                    'description'  : product.dinning.description,
                    'food_type'    : product.dinning.food_type.name,
                    'dinning_type' : product.dinning.dinning_type.name
                    }

            product_list.append(dinning)

            return JsonResponse({'data' : product_list}, status=200)
