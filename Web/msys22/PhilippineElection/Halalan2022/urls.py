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

urlpatterns=[
path('', views.login_person, name='login'),
path('logout', views.logout, name='logout'),
path('create_account', views.signup, name='signup'),
path('error',views.youcant,name='youcant'),
path('home', views.home, name='home'),
path('users',views.users, name='users'),
path('update/<int:pk>/', views.update, name='update'),
path('candidates',views.candidates, name='candidates'),
path('vote',views.vote, name='vote'),
path('votepage/<int:pk>/',views.votepage, name='votepage'),
path('about',views.about, name='about'),
]