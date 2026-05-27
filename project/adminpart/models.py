from django.db import models
from myapp.models import Restaurant
# Create your models here.
class RestaurentOwner(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    restaurants = models.ManyToManyField(
        Restaurant,
        related_name = 'owners'
    )
    def __str__(self):
        return f"{self.name} {self.surname}"

class Employee(models.Model):
    restaurants = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='employees',
    )
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    hire_date = models.DateField()
    def __str__(self):
        return f"{self.name} {self.surname}"
