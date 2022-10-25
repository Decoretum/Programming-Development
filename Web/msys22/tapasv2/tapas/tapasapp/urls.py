from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_person, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('error', views.error, name='error'),
    path('basic_list', views.basic_list, name='basic_list'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('change_password/<int:pk>/', views.change, name='change'),
    path('better_menu', views.better_menu, name='better_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
    path('view_detail/<int:pk>/', views.view_detail, name='view_detail'),
    path('delete_dish/<int:pk>/', views.delete_dish, name='delete_dish'),
    path('update_dish/<int:pk>/', views.update_dish, name='update_dish'),
]