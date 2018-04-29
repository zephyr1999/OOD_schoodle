from django.db import models
from .person import Person
from .grade import Grade
from .content_item_collection import ContentItemCollection

class Student(models.Model, Person):
    grades = models.ManyToManyField(Grade)
    content = models.OneToOneField(ContentItemCollection)
