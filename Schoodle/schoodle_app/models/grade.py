from django.db import models
from .course import Course

class ContentItem(models.Model):
	#data members
	grade = models.FloatField(default=0.0)
	description = models.CharField(max_length=1000)
	associatedCourse = models.OneToMany(ContentItem)

	def setGrade(gradeInput):
		self.grade = gradeInput

	def getGrade():
		return self.grade