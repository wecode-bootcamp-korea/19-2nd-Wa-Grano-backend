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
    if request.method == "GET":
        destinations = Category.objects.get(id=category_id).destination.all()

        data = [{
            'name': destination.name,
            'image_url': destination.image_url
            } for destination in destinations]



























