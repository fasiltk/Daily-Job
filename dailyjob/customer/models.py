from django.db import models
from authsystem.models import *
# Create your models here.

class Book(models.Model):
    labour=models.ForeignKey(Labour, on_delete=models.CASCADE)
    cust_username=models.CharField(max_length=100)
    date=models.DateField(unique=True)
    location_name=models.CharField(max_length=100)
    b_address=models.TextField()
    b_profession=models.CharField(max_length=100,null=True)
    b_fees = models.CharField(max_length=10,default=0,null=True)
    confirm=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.labour.name}"
