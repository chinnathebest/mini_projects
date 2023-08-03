from django.db import models

# Create your models here.
class food_items(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')
    price = models.IntegerField()
    discount = models.BooleanField(default=False)

class noticebord(models.Model):
    name =models.CharField(max_length=50)
    
