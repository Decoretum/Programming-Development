from django.db import models
import decimal

# Create your models here.
class item(models.Model): #Once you migrated this, it will create a appname_table on MySQL Table in database
    item_name = models.CharField(max_length=100)
    #itemid = models.AutoField(200, primary_key=True)
    item_price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.CharField(max_length=500)
    stock_quantity = models.IntegerField(default=0)
    outofstock = models.BooleanField(default=False) # 0 is false, 1 is true
    object = models.Manager()

    def CheckStock(self):
        return self.stock_quantity <= 0
    
    def getStock(self):
        return self.stock_quantity
    
    def getName(self):
        return self.item_name
    
    def getPrice(self):
        return self.item_price
    
    def getDesc(self):
        return self.description
    
    def __str__(self):
        return "Product: " + str(self.pk) + "\n" + "Name: " + str(self.item_name) 
    

class order(models.Model):
    amountpaid = models.DecimalField(decimal_places=2, max_digits=7)
    orderdate = models.DateField(auto_now_add=True)
    paymenttype = models.CharField(default='', max_length=200)
    object = models.Manager()

class item_order(models.Model):
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    line_total = models.DecimalField(decimal_places=2, max_digits=7)
    quantity = models.IntegerField(default=0)
    object = models.Manager()



