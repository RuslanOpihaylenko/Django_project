from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Restaurant, Specialization, RestaurantImage, Review

admin.site.register(Restaurant)
admin.site.register(Specialization)
admin.site.register(RestaurantImage)
admin.site.register(Review)