from django.db import models
from .person import Person

class Course(models.Model):
    #data members
    name = models.CharField(max_length=200)
    # This definition actually means one person has many courses
    p = models.ManyToManyField(Person)

    #class functions
    def __str__(self):
        #default tostring
        return self.name
