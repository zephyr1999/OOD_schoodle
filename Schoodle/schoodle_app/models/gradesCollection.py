from django.db import models
from .grade import Grade

class GradesCollection(models.Model):
	#data members
	gradesList = models.OneToMany(Grade)

	def addGrade(g):
		gradesList.append(g)

	def getGrade(g):
		for grade in gradesList:
			if grade == g:
				return grade