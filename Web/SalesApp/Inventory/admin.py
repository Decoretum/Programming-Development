from django.contrib import admin
from . models import Product, Userperson, OrderedProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(Userperson)
admin.site.register(OrderedProduct)