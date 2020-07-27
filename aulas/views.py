from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse

from .models import Aula


def index(request):
     names = Aula.objects.all().values_list('name', flat=True)
     return JsonResponse(list(names), safe=False)
    #return HttpResponse("Hello, world. You're at the polls index.")