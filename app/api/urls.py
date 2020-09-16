from django.urls import path
from api.views import brick,broker,cart,property

urlpatterns = [
    path('property/', property.getAllPropertys),
    path('property/<int:property>/', property.getProperty),
    path('property/brick/<int:property>/', property.brickProperty),

    path('brick/', brick.getAllBricks),
    path('brick/<int:idBrick>/', brick.getBrick),

    path('broker/',broker.getBrocker),

    path('cart/', cart.default),
    path('cart/<int:broker>/', cart.cart),
    path('cart/add/', cart.add),
    path('cart/delete/', cart.delete),
    path('cart/checkout/', cart.checkout),
]