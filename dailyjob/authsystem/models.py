from django.db import models

# Create your models here.

class Labour(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    fees = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/images/')
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    verification=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Profession(models.Model):
    labour=models.ForeignKey(Labour, on_delete=models.CASCADE)
    profession=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.labour.name} - {self.profession}"


class Date(models.Model):
    labour=models.ForeignKey(Labour, on_delete=models.CASCADE)
    date = models.DateField(unique=True)

    def __str__(self):
        return f"{self.labour.name} - {self.date}"


class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    address=models.TextField()
    image = models.ImageField(upload_to='images/')
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"