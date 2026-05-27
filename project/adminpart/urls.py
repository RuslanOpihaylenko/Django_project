from django.urls import path

from . import views


urlpatterns = [

    path(
        'owners/',
        views.owners_list,
        name='owners_list'
    ),

    path(
        'employees/<str:restaurant_name>/',
        views.employees_by_restaurant,
        name='employees'
    ),
]