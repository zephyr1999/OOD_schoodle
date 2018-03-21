from django.db import models

class Person(models.Model):
    # data members
    name = models.CharField(max_length=200)

    # functions
    def __str__(self):
        #default tostring method
        return self.name
