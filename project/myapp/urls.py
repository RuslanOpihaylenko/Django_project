from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', views.restaurant_list, name='restaurant_list'),
   path('add/', views.add_restaurant, name='add_restaurant'),
   path('delete/<int:id>/',
        views.delete_restaurant,
        name='delete_restaurant'),

   path('edit/<int:id>/',
        views.edit_restaurant,
        name='edit_restaurant'),

   path('review/<int:id>/',
        views.add_review,
        name='add_review'),
   path('register/', views.register, name='register'),

   path(
    'login/',
    LoginView.as_view(
        template_name='login.html',
        next_page='restaurant_list'
    ),
    name='login'
    ),

   path(
    'logout/',
    LogoutView.as_view(next_page='restaurant_list'),
    name='logout'
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
