import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from api.models import Brick

@csrf_exempt
def getAllBricks(request):
    if(request.method != 'GET'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    data = []
    bricks = Brick.objects.filter(active=True)

    for brick in bricks:
        data.append({
            'id':brick.id,
            'price': brick.price,
            'existence': brick.existence,
            'property': brick.property.name,
            'broker': brick.broker.name
        })

    return JsonResponse({'propertys':data})

@csrf_exempt
def getBrick(request,idBrick):
    if(request.method != 'GET'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    print(idBrick)
    brick = Brick.objects.get(id=idBrick,active=True)
    data = {
        'id':brick.id,
        'price': brick.price,
        'existence': brick.existence,
        'property': brick.property.id,
        'propertyName': brick.property.name,
        'broker': brick.broker.id,
        'brokerName': brick.broker.name
    }

    return JsonResponse(data)