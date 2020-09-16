import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from api.models import Property,Broker,Brick,Cart,BrockerBricks

@csrf_exempt
def default(request):
    if(request.method != 'GET'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    return JsonResponse({'message':''})

@csrf_exempt
def cart(request,broker):
    if(request.method != 'GET'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    try:
        myCart = Cart.objects.filter(broker__id=broker,checkout=False,deleted=False)
        if(len(myCart)<=0):
            return JsonResponse({'message':'you not have products yet'})

        data = []
        total = 0
        for item in myCart:
            data.append({
                'property':item.brick.property.name,
                'brickId':item.brick.id,
                'price': item.brick.price,
                'quantity': item.quantity,
            })
            total += item.brick.price*item.quantity

        response = {
            'id': myCart[0].broker.id,
            'name': myCart[0].broker.name,
            'items':data,
            'total': total
        }

        return JsonResponse(response)
    except:
        return HttpResponseBadRequest(
            f'Error during exect',
            status=400
        )

@csrf_exempt
def add(request):
    if(request.method != 'POST'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    try:
        requestData = json.loads(request.body)
        response = {}

        if not(
            Broker.objects.filter(id=requestData['idBroker'],active=True).exists() and 
            Brick.objects.filter(id=requestData['idBrick'],active=True).exists()
        ):
            return HttpResponseBadRequest(
                'Invalid request',
                status=400
            )

        if(Cart.objects.filter(
            broker__id=requestData['idBroker'],
            brick__id=requestData['idBrick'],
            checkout=False,
            deleted=False
        ).exists()):
            item = Cart.objects.get(
                broker__id=requestData['idBroker'],
                brick__id=requestData['idBrick'],
                checkout=False,
                deleted=False
            )
            item.quantity += requestData['quantity']
        else:
            item = Cart.objects.create(
                quantity = requestData['quantity'],
                brick = Brick.objects.get(id=requestData['idBrick']),
                broker = Broker.objects.get(id=requestData['idBroker'])
            )
        response['quantity'] = item.quantity
        response['brick'] = item.brick.id
        response['broker'] = item.broker.id
        item.save()

        return JsonResponse(response)
    except:
        return HttpResponseBadRequest(
            f'Error during exect',
            status=400
        )

@csrf_exempt
def delete(request):
    if(request.method != 'POST'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )
    try:
        requestData = json.loads(request.body)
        response = {}

        if(Cart.objects.filter(
            broker__id=requestData['idBroker'],
            brick__id=requestData['idBrick'],
            checkout=False,
            deleted=False
        ).exists()):
            item = Cart.objects.get(
                broker__id=requestData['idBroker'],
                brick__id=requestData['idBrick'],
                checkout=False,
                deleted=False
            )
            item.deleted = True
        
        response['quantity'] = item.quantity
        response['brick'] = item.brick.id
        response['broker'] = item.broker.id
        response['deleted'] = item.deleted
        item.save()

        return JsonResponse(response)
    except:
        return HttpResponseBadRequest(
            f'Error during exect',
            status=400
        )

@csrf_exempt
def checkout(request):
    if(request.method != 'POST'):
        return HttpResponseBadRequest(
            'This view can not handle method {0}'.format(request.method),
            status=405
        )

    requestData = json.loads(request.body)
    response = {}

    myCart = Cart.objects.filter(broker__id=requestData['idBroker'],checkout=False,deleted=False)
    if(len(myCart)<1):
        return JsonResponse({'message':'You not have products in cart'})
    for itemFromCart in myCart:
        item = Cart.objects.get(
            id=itemFromCart.id
        )
        reduceExistence(item.brick.id,int(item.quantity))
        addBrickToBrocker(int(item.quantity),item.brick.property,item.broker)
        item.checkout = True
        item.save()
    return JsonResponse({'message':'the products already checkout'})

def reduceExistence(id,quantity):
    brick = Brick.objects.get(id=id)
    brick.existence -= quantity
    brick.save()

def addBrickToBrocker(quantity,property,broker):
    if(BrockerBricks.objects.filter(quantity=quantity,property=property).exists()):
        brokerBrick = BrockerBricks.objects.get(quantity=quantity,property=property)
        brokerBrick.quantity += quantity
        brokerBrick.save()
    else:
        newBrick = BrockerBricks.objects.create(quantity=quantity,property=property,broker=broker)
        newBrick.save()
