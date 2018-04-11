from django.db import models

class FileItem(models.Model):
	# data members
	contentPath = models.CharField(max_length=200)

	def __str__(self):
		#default tostring
		return self.contentPath