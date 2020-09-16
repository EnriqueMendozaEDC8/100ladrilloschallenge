import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from api.models import Broker

@csrf_exempt
def getBrocker(request):
    if(request.method != 'POST'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    try:
        requestData = json.loads(request.body)
        brocker = Broker.objects.get(email=requestData['email'],active=True)

        return JsonResponse({'id':brocker.id,'email':brocker.email,'name':brocker.name})
    except:
        return HttpResponseBadRequest(
            f'Error during exect',
            status=400
        )