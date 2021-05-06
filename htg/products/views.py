import json

from django.views import View
from django.http  import HttpResponse, JsonResponse, 

from .models import Product, Destination,ProductImage, 


class Popular_Destinations(View):
    def get(self,request):

        'popular_hotel'       : [i.name for i in Product.objects.filter(is_dinning=0).order_by('-rating','price')[0:5]] 
        'popular_hotel_image' : j.image_url for j
        in a.productimage_set.all()) 
        for a in Product.objects.filter(is_dinning=0).order_by('-rating','price')[0:5]]

                            [[<ProductImage: ProductImage object (25)>,
                                <ProductImage: ProductImage object (26)>],
                            [<ProductImage: ProductImage object (9)>,
                             <ProductImage: ProductImage object (10)>],
                            [<ProductImage: ProductImage object (1)>,
                            <ProductImage: ProductImage object (2)>],
                            [<ProductImage: ProductImage object (37)>,
                            <ProductImage: ProductImage object (38)>],
                            [<ProductImage: ProductImage object (15)>,
                            <ProductImage: ProductImage object (16)>]]

                                                or

        'popular_hotel_image' : [a.productimage_set.all() for a in Product.objects.filter(is_dinning=0).order_by('-rating','price')[0:5]]
                        [<QuerySet [<ProductImage: ProductImage object (25)>, <ProductImage: ProductImage object (26)>]>,
                        <QuerySet [<ProductImage: ProductImage object (9)>, <ProductImage: ProductImage object (10)>]>,
                        <QuerySet [<ProductImage: ProductImage object (1)>, <ProductImage: ProductImage object (2)>]>,
                        <QuerySet [<ProductImage: ProductImage object (37)>, <ProductImage: ProductImage object (38)>]>,
                        <QuerySet [<ProductImage: ProductImage object (15)>, <ProductImage: ProductImage object (16)>]>]
                        return HttpResponse(status=200)
        return JsonResponse({'message':'KEY_ERROR'}) 





class DinningView(View): # 부산에 찍히는 숙소와 레스토랑 리스트 출력
    def get(self,request, product_id=None):
        
        if not Product.objects.get(id=product_id):


            products = Product.objects.get(is_dinning=1)

        dinnings = [
            {
                'id'     : product.id
                'rating' : product.rating
                'address' : product.address
                'description' : product.description
                'image'       : [image.ProductImage for image in products.ProductImage_set.all()]
                'latitude'    : product.latitude
                'longitude'   : product.longitude
                }for product in Product.objects.all()]
        
            return HttpResponse(status=200)
        return JsonResponse({'message':'KEY_ERROR'})




class ThisIsHotPlaces(View):
    def get(self,request):

        destinations = Destination.objects.get(id=1)

        hotplaces = [
                {


                    }]



