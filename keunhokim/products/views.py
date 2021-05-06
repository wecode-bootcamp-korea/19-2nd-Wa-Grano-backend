from django.views import View
from .models      import *
from django.http  import HttpResponse,JsonResponse

def category(request):
    if request.method == "GET":
        categories = Category.objects.all()

        data = [{
            'name'     : category.name,
            'image_url': category.image_url
        } for category in Category.objects.all()]

        return JsonResponse({'data':data},status=200)

def destination(request,category_id):
    if request.method == "GET":
        destinations = Category.objects.get(id=category_id).destination.all()

        data = [{
            'name': destination.name,
            'image_url': destination.image_url
            } for destination in destinations]



























