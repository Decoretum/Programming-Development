from django.shortcuts import render, redirect
from .models import item, order, item_order
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.contrib import messages


# Create your views here.
def hello(request): #displays all items
    items = item.object.all()
    length = len(items)
    return render(request,'A1/hello_world.html',{
        'len' : length,
        'I' : items
    })

def viewOrders(request):
    orders = order.object.all()
    itemorders = item_order.object.all()
    length = len(orders)
    return render(request, 'A1/orders.html',{
        'O' : orders,
        'IO' : itemorders,
        "L" : length
    })

def add(request): #adds product
    request.session['status'] = "ADD"
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        stock_quantity = request.POST.get('stock')
        object = item.object.create(
            item_name = name,
            item_price = price,
            description = desc,
            stock_quantity = stock_quantity
        )
        object.save()
        return redirect('home')
        
    else:
        return render(request, 'A1/add.html',{
            'status' : request.session.get('status')
        })
    
def edit(request, pk):
    request.session['status'] = "EDIT"
    obj = get_object_or_404(item, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        stock = request.POST.get('stock')
        if stock.strip() == "":
            stock = 0
        obj.item_name = name
        obj.item_price = price
        obj.description = desc
        obj.stock_quantity += int(stock)
        obj.outofstock = obj.CheckStock()
        obj.save()
        return redirect('home')
    else:
        return render(request,'A1/add.html',{
            'status' : request.session.get('status'),
            'obj' : obj
        })

def delete(request,pk):
    obj = get_object_or_404(item, pk=pk)
    obj.delete()
    return redirect('home')

#def recurs(request, remnant):
    

def confirm_order(request):
    items = item.object.filter(stock_quantity__gte = 1)
    length = len(items)
    if request.method == 'POST':
        #totalamount = Decimal(str(request.POST.get('total_amount')[1:]))
        totalamount = request.POST.get('total_amount')
        paymentmethod = request.POST.get('payment_method')
        completeorder = request.POST.get('complete_order')
   
        if totalamount == "" or paymentmethod == None:
            messages.info(request, 'No product chosen, or payment methods is null')
            return redirect('order')
        else:
            totalamount = totalamount[1:]
        item_fixed = completeorder[:-1]
        item_array = item_fixed.split("-")

            

        ord = order.object.create(
            amountpaid = totalamount,
            paymenttype = paymentmethod
        )

        ord.save()

        for i in item_array:
            obj = item.object.get(pk=i[0])
            objprice = obj.getPrice()

            #Get full quantity
            j = len(i)-1
            final = ""
            while True:
                if i[j] != " ":
                    final += i[j]
                    j -= 1
                else:
                    break
            
            final = final[::-1]
            total = Decimal(objprice * int(final))

            obj.stock_quantity -= int(final)
            obj.outofstock = obj.CheckStock()
            obj.save()

            hybrid = item_order.object.create(
                item_id = obj,
                order_id = ord,
                line_total = total,
                quantity = int(final)
            )
            hybrid.save()

        return redirect('orders')
    else:
        return render(request, 'A1/confirm.html',{
            'I' : items,
            'L' : length
        })