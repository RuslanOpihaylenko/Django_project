from django.shortcuts import render
from .models import RestaurentOwner, Employee


def owners_list(request):

    owners = RestaurentOwner.objects.all()

    return render(request, 'owners_list.html', {
        'owners': owners
    })


def employees_by_restaurant(request, restaurant_name):

    employees = Employee.objects.filter(
        restaurants__name__icontains=restaurant_name
    )

    return render(request, 'employees.html', {
        'employees': employees,
        'restaurant_name': restaurant_name
    })