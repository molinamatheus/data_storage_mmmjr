from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from fruits.models import Fruit, Region
from fruits.serializers import FruitSerializer, RegionSerializer
# Create your views here.

@csrf_exempt
def fruits_list(request, pk=None):
    """
    Fruits CRUD
    """
    if pk is not None:
        try:
            fruit = Fruit.objects.get(pk=pk)
        except Fruit.DoesNotExist:
            return HttpResponse(status=404)

    if request.method == 'GET':
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FruitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FruitSerializer(fruit, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        fruit.delete()
        return HttpResponse(status=204)

@csrf_exempt
def region_list(request, pk=None):
    """
    Regions CRUD
    """
    if pk is not None:
        try:
            region = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return HttpResponse(status=404)

    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegionSerializer(region, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        print(f"{region} is gonna be deleted")
        region.delete()
        return HttpResponse(status=204)