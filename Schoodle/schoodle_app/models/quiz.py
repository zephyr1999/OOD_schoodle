from django.db import models
from .question import Question

class Question(models.Model):
    # data members
    questions = models.OneToMany(Question)
    name = models.CharField(max_length=200)
