from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    trigger1 = models.BooleanField()
    trigger2= models.BooleanField()

    def __str__(self):
        return self.name