from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    std = models.IntegerField()
    section = models.CharField(max_length=5)
    address = models.TextField()

    def __str__(self):
        return "{}-{}".format(self.name, self.std)
