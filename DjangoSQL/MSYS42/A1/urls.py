from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('AddProduct', views.add, name='add'),
    path('EditProduct/<int:pk>', views.edit, name='edit'),
    path('Deleted/<int:pk>', views.delete, name='delete'),
    path('AddOrder', views.confirm_order, name='order'),
    path('Orders', views.viewOrders, name='orders')
]

