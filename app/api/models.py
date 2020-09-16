from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    detail = models.TextField()
    highProfitability = models.FloatField()
    lowProfitability = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Broker(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Brick(models.Model):
    price = models.FloatField()
    existence = models.PositiveIntegerField()
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    ) 
    broker = models.ForeignKey(
        Broker,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.price)

class BrockerBricks(models.Model):
    quantity = models.PositiveIntegerField()
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    ) 
    broker = models.ForeignKey(
        Broker,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.quantity)

class Cart(models.Model):
    quantity = models.PositiveIntegerField()
    brick = models.ForeignKey(
        Brick,
        on_delete=models.CASCADE
    )
    broker = models.ForeignKey(
        Broker,
        on_delete=models.CASCADE
    )
    checkout = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)