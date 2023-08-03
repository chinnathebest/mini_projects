from django.db import models

# Create your models here.
class datas(models.Model):
    name=models.CharField(max_length=20)
    age = models.IntegerField()
    description = models.TextField()
    data =models.DateField(auto_now=True)

    def __str__(self):
        return self.name
