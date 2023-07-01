from django.db import models

# Create your models here.





class Dish(models.Model):
    dishId = models.IntegerField()
    restaurantName = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    items= models.JSONField()
    lat_long = models.CharField(max_length=30)
    detail = models.JSONField()


    