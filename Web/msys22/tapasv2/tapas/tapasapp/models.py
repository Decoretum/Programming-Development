from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=300)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.name

class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = models.Manager()

    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password

    def __str__(self):
        return 'username' + ':' + str(self.username) + '   ' + 'password' + ':' +  str(self.password)

    