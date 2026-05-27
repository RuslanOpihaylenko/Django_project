from django.contrib import admin

# Register your models here.
from .models import RestaurentOwner, Employee

admin.site.register(RestaurentOwner)
admin.site.register(Employee)