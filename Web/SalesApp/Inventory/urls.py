from django.urls import path
from . import views

urlpatterns=[
path('',views.home,name='home'),
path('Products',views.Products, name='Products')
#path('Order',views.Order, name='Order')

]