from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=30)
    phone=models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)