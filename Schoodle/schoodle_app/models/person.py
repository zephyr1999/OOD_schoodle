from django.db import models
from .course import Course

class Person(models.Model):
    # data members
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)

    # functions
    def __str__(self):
        #default tostring method
        return self.name

    def get_ID(self):
        return self.id
