from django.contrib import admin
from .models import Position,Candidate,Userperson,Vote


# Register your models here.
admin.site.register(Position)
admin.site.register(Candidate)
admin.site.register(Userperson)
admin.site.register(Vote)