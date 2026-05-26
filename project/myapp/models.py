from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    specializations = models.ManyToManyField(Specialization)
    address = models.TextField()
    website = models.URLField(blank=True)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='restaurants/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Фото для {self.restaurant.name}"
class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Отзыв от {self.author.username}"
