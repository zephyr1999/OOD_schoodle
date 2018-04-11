from django.db import models
from .student import Student
from .instructor import Instructor
from .quiz import Quiz

class Course(models.Model):
    #data members
    name = models.CharField(max_length=200)
    # This definition actually means one person has many courses
    persons = models.ManyToManyField(Person)
    students = models.ManyToManyField(Student)
    instructors = models.ManyToManyField(Instructor)
    quizzes = models.ManyToManyField(Quiz)

    #class functions
    def __str__(self):
        #default tostring
        return self.name

    def get_ID(self):
        return self.id
