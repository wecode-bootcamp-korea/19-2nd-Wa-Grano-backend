from django.views import View
from .models      import *
from django.http  import HttpResponse,JsonResponse

#def category(request):
#    if request.method == "GET":
#        data = {
#            'category':
#        }





def DestinationMain(request):
    if request.method == 'GET':
        districts = City.objects.get(name='부산').district_set.all()

        data = {
            'name'     : [district.name for district in districts],
            'image_url': [district.image_url for district in districts]
        }

        return JsonResponse({'data':data},status=200)





