from django.db import models
from .person import Person
from .course import Course

class ContentItem(models.Model):
	#data members
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	#One to one associations with person and course
	author = models.OneToOne(Person)
	associatedCourse = models.OneToOne(Course)

	def __str__ (self):
		#default tostring
		return self.name

	def viewContent(self):
		return self.description