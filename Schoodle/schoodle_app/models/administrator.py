from django import models
from .person import Person

class Administrator(models.Model, Person):
    # admin has no attributes beyond person
    # but has several course managment style methods

    def add_student(self,s,c):
        #add student s to course c
        c.students.add(s)
        c.save()

    def add_instructor(self,i,c):
        #add instructor i to course c
        c.instructors.add(i)
        c.save()

    def remove_student(self,s,c):
        #remove s from c
        c.students.remove(s)
        c.save()

    def remove_instructor(self,i,c):
        #remove i from c 
        c.instructors.remove(i)

