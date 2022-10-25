from django.urls import path
from . import views


urlpatterns = [
    path('', views.better_menu, name='better_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
    path('view_detail/<int:pk>/', views.view_detail, name='view_detail'),
    path('delete_dish/<int:pk>/', views.delete_dish, name='delete_dish'),
    path('update_dish/<int:pk>/', views.update_dish, name='update_dish'),
]