from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Kompyuter(models.Model):
    kompyuter_name=models.CharField(max_length=50)
    windows_number=models.IntegerField()
    price=models.IntegerField()


    def __str__(self):
        return self.kompyuter_name
