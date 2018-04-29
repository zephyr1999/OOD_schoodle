from django.db import models
from .course import Course
from .grade import Grade
from .content_item_collection import ContentItemCollection

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

class Student(models.Model, Person):
    grades = models.ManyToManyField(Grade)
    content = models.OneToOneField(ContentItemCollection)

