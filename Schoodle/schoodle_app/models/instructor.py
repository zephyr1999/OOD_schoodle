from django import models
from .person import Person
from .content_item_collection import ContentItemCollection

class Instructor(models.Model, Person):
    #instructor only has one additional field to person base class
    content = models.OneToOneField(ContentItemCollection)

