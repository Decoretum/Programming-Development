from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# I hereby attest to the truth of the following facts:
# I have not discussed the <programming language used> language code in my program with anyone other than my instructor or the teaching assistants assigned to this course.
# I have not used <programming language used> language code obtained from another student, or any other unauthorized source, either modified or unmodified.
# If any <programming language used> language code or documentation used in my program was obtained from another source, such as a text book or course notes, that has been clearly noted with a proper citation in the comments of my program.


class Position(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager() 

    def getName(self):
        return self.name

    def __str__(self):
        return 'Position Name' + ':' + ' ' + str(self.name)

class Candidate (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    slogan = models.CharField(max_length=500)
    position_id = models.ForeignKey(Position, null=True, blank=True, on_delete=models.CASCADE)
    objects = models.Manager()


    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getNickname(self):
        return self.nickname
    
    def getSlogan(self):
        return self.slogan
    
    def __str__(self):
        return 'PK' + ':' + ' ' + 'Candidate ' + str(self.pk) + ':' + ' ' + str(self.position_id) + ',' + ' ' + str(self.first_name) + ' ' + str(self.last_name)  + ',' + ' ' + str(self.nickname) + ',' + ' ' + str(self.slogan)



class Userperson(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.CharField(max_length=50)
    objects = models.Manager()

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
    
    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name

    def getBirthday(self):
        return self.birthday

    def getSex(self):
        return self.sex

    def __str__(self):
        return 'pk' + ':' + ' ' + 'User ' + str(self.pk) + ':' + ' ' + str(self.username) + ',' + ' ' + str(self.first_name) + ' ' + str(self.last_name) + ',' + ' ' + str(self.birthday) + ',' + ' ' + str(self.sex)



class Vote(models.Model):
    user_id = models.ForeignKey(Userperson, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000,default='Add Comments')
    objects = models.Manager()

    def getComment(self):
        return self.comment

    def __str__(self):
        return 'pk' + ':' + ' ' + str(self.pk) + ':' + ' ' + str(self.candidate_id.position_id.name) + ':' + ' ' + 'Candidate' + ':' + ' ' + str(self.candidate_id.first_name) + ' ' + str(self.candidate_id.last_name) + '.' + ' ' + str(self.comment)
