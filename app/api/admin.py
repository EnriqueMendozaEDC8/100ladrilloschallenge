from django.contrib import admin
from .models import Property,Broker,Brick,Cart,BrockerBricks
# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'detail','highProfitability','lowProfitability','active')

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    fields = ('name','email','active')

@admin.register(Brick)
class BrickAdmin(admin.ModelAdmin):
    fields = ('price','existence','property','broker','active')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ('quantity','brick','broker','checkout','deleted')
    
@admin.register(BrockerBricks)
class BrockerBricksAdmin(admin.ModelAdmin):
    fields = ('quantity','property','broker','active')