from django.shortcuts import render
from .models import Dish

#I hereby attest to the truth of the following facts:
#- I have not discussed the <programming language used> language code in my program
# with anyone other than my instructor or the teaching assistants assigned to this course.
# - I have not used <programming language used> language code obtained from another
# student, or any other unauthorized source, either modified or unmodified.
# - If any <programming language used> language code or documentation used in my
# program was obtained from another source, such as a text book or course notes, that has
# been clearly noted with a proper citation in the comments of my program. 

# Create your views here.

def view_basic_list(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/basic_list.html', {'dishes':dish_objects})


def view_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/list.html', {'dishes':dish_objects})

def add_menu(request):
    return render(request,'tapasapp/add_menu.html')