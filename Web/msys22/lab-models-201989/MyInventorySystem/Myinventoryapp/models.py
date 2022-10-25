from django.db import models

# Create your models here.

# I hereby attest to the truth of the following facts:
# I have not discussed the <programming language used> language code in my program with anyone other than my instructor or the teaching assistants assigned to this course.
# I have not used <programming language used> language code obtained from another student, or any other unauthorized source, either modified or unmodified.
# If any <programming language used> language code or documentation used in my program was obtained from another source, such as a text book or course notes, that has been clearly noted with a proper citation in the comments of my program.

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

class Supplier(models.Model):
    Name = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    Country = models.CharField(max_length=500)
    CreatedAt = models.CharField(max_length=500)
    objects = models.Manager()

    def getName(self):
        return self.Name
    def __str__(self):
        return self.Name + ' ' + '*' + ' ' + self.City + ',' + ' ' + self.Country + ' ' + 'created at:' + ' ' + self.CreatedAt

class WaterBottle(models.Model):
    SKU = models.CharField(max_length=500)
    Brand = models.CharField(max_length=500)
    Cost = models.CharField(max_length=500)
    Size = models.CharField(max_length=500)
    MouthSize = models.CharField(max_length=500)
    Color = models.CharField(max_length=500)
    Suppliedby = models.CharField(max_length=500) #Supplier
    CurrentQuantity = models.CharField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ' ' + str(self.SKU) + ':' + ' ' + str(self.Brand) + ',' + ' ' + str(self.MouthSize) + ',' + ' ' + str(self.Size) + ',' + ' ' + str(self.Color) + ',' + ' ' + 'supplied by' + ' ' + str(self.Suppliedby) + ',' + ' ' + str(self.Cost) + ' ' + ':' + ' ' + str(self.CurrentQuantity)