from django.db import models

class NewsItem(models.Model):
	# data members
	news = models.CharField(max_length=200)

	def __str__(self):
		#default tostring
		return self.news