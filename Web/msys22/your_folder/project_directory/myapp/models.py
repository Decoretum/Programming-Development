from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=500)
    classification = models.CharField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ':' + str(self.name) + ',' + str(self.classification)


# Create your models here.
