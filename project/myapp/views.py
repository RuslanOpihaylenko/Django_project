from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, RestaurantImage, Specialization
from .forms import RestaurantForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)

        files = request.FILES.getlist('images')

        if form.is_valid():
            restaurant = form.save()

            for file in files:
                RestaurantImage.objects.create(
                    restaurant=restaurant,
                    image=file
                )

            return redirect('restaurant_list')

    else:
        form = RestaurantForm()

    return render(request, 'add_restaurant.html', {
        'form': form
    })


def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'restaurant_list.html', {
        'restaurants': restaurants
    })


def restaurant_list(request):

    query = request.GET.get('q')

    if query:
        restaurants = Restaurant.objects.filter(
            specializations__name__icontains=query
        ).distinct()
    else:
        restaurants = Restaurant.objects.all()

    return render(request, 'restaurant_list.html', {
        'restaurants': restaurants
    })
def delete_restaurant(request, id):

    restaurant = get_object_or_404(Restaurant, id=id)

    restaurant.delete()

    return redirect('restaurant_list')

def edit_restaurant(request, id):

    restaurant = get_object_or_404(Restaurant, id=id)

    if request.method == 'POST':

        form = RestaurantForm(
            request.POST,
            instance=restaurant
        )

        if form.is_valid():
            form.save()

            return redirect('restaurant_list')

    else:
        form = RestaurantForm(instance=restaurant)

    return render(request, 'edit_restaurant.html', {
        'form': form
    })

@login_required
def add_review(request, id):

    restaurant = get_object_or_404(Restaurant, id=id)

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.restaurant = restaurant
            review.author = request.user

            if request.user.is_authenticated:
                review.approved = True
            else:
                review.approved = False

            review.save()

            return redirect('restaurant_list')

    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {
        'form': form,
        'restaurant': restaurant
    })
def page_not_found(request, exception):
    return render(request, 'Not_found.html')

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('restaurant_list')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {
        'form': form
    })