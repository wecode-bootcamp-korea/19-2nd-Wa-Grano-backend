from django.views import View
from django.http  import JsonResponse, HttpResponse

from .models import Destination, Product

# 메인페이지에 인기여행지 리스트 전체 view
class Destination(View):
    def get(self, request):
        
        try: 
            destination = [
                    {
                        'name' : destination.name,
                        'image_url' : destination.image_url
                        } for destination in Destination.objects.all()
                    ]
            return JsonResponse({'data' : destination}, status=200)
        
        except:
            return JsonResponse({'message' : 'error'}, status=400)

# 레스토랑도 할인 받으세요! 레스토랑 리스트 전체 뿌려주는 view
class BestSeller(View):
    def get(self, request):

        
        hotel = [
                {
                    'name' : hotel.name,
                    'rating' : hotel.rating,
                    'price' : hotel.price,
                    'image' : [image.image_url for image in hotel.productimage_set.all()]
            } for hotel in Product.objects.order_by('rating').filter(category_id=2)[:3]
                ]

        restaurant_dinning = [
                {
                    'name' : restaurant.name,
                    'rating' : restaurant.rating,
                    'price' : restaurant.price,
                    'image' : [image.image_url for image in restaurant.productimage_set.all()]
                    } for restaurant in Product.objects.filter(category_id=4)[:3]
                ]

        attraction_activity = [
                {
                    'name' : activity.name,
                    'rating' : activity.rating,
                    'price' : activity.price,
                    'image' : [image.image_url for image in activity.productimage_set.all()]
                    } for activity in Product.objects.filter(category_id=3)[:3]
                ]
        
        return JsonResponse(
                {
                    'activity_experience' : hotel,
                    'restaurant_dinning' : restaurant_dinning,
                    'attraction_activity' : attraction_activity
                    }, status=200
                )
