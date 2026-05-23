from django import forms
from .models import Restaurant, RestaurantImage, Review


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'specializations',
            'address',
            'website',
            'contact_number'
        ]

        widgets = {
            'specializations': forms.CheckboxSelectMultiple()
        }


class RestaurantImageForm(forms.ModelForm):
    class Meta:
        model = RestaurantImage
        fields = ['image']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text']