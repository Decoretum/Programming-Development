from django.urls import path
from . import views

#I hereby attest to the truth of the following facts:
#- I have not discussed the <programming language used> language code in my program
# with anyone other than my instructor or the teaching assistants assigned to this course.
# - I have not used <programming language used> language code obtained from another
# student, or any other unauthorized source, either modified or unmodified.
# - If any <programming language used> language code or documentation used in my
# program was obtained from another source, such as a text book or course notes, that has
# been clearly noted with a proper citation in the comments of my program. 

urlpatterns = [
    path('basic_list', views.view_basic_list, name='view_basic_list'),
    path('', views.view_menu, name='view_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
]