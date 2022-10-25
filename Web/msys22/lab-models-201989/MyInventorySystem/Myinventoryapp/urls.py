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
    path('', views.login_person, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('view_supplier', views.view_supplier, name='view_supplier'),
    path('view_bottles', views.view_bottles, name='view_bottles'),
    path('add_bottle', views.add_bottle, name='add_bottle'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('change_password/<int:pk>/', views.change, name='change'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('view_normal', views.view_normal, name='view_normal'),
    path('view_details/<int:pk>/', views.view_details, name='view_details'),
    path('update_bottle/<int:pk>/', views.update_bottle, name='update_bottle'),
    path('delete_bottle/<int:pk>/', views.delete_bottle, name='delete_bottle'),
]