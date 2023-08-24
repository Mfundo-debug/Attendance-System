from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()