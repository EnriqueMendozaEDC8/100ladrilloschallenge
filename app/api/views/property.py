import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from api.models import Property, Brick

@csrf_exempt
def getAllPropertys(request):
    if(request.method != 'GET'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    data = []
    propertys = Property.objects.filter(active=True)

    for porperty in propertys:
        data.append({
            'id': porperty.id,
            'name': porperty.name,
            'location': porperty.location,
            'detail': porperty.detail,
            'highProfitability': porperty.highProfitability,
            'lowProfitability': porperty.lowProfitability,
        })

    return JsonResponse({'propertys':data})

@csrf_exempt  
def getProperty(request,property):
    if(request.method != 'GET'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    porperty = Property.objects.get(id=property,active=True)
    data = {
        'id': porperty.id,
        'name': porperty.name,
        'location': porperty.location,
        'detail': porperty.detail,
        'highProfitability': porperty.highProfitability,
        'lowProfitability': porperty.lowProfitability,
    }

    return JsonResponse(data)
    
@csrf_exempt
def brickProperty(request,property):
    if(request.method != 'GET'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    porperty = Brick.objects.get(property__id=property,active=True)
    data = {
        'id':porperty.id
    }

    return JsonResponse(data)