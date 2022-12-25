from django.urls import path
from . import views

urlpatterns=[
path('home',views.home,name='home'),
path('Products',views.Products, name='Products'),
path('',views.Signup, name='Signup'),
path('Login', views.Login, name='Login'),
path('User', views.Users, name='User'),
path('logout', views.logout, name='logout'),
path('order/<int:pk>/', views.Order, name='order'),
path('Developer', views.Developer, name='Developer')

]