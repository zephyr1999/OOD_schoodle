from django.db import models
from .contentItem import ContentItem

class ContentItemFactory(models.Model):
	contentItem = models.CharField(max_length=200)

	def createContent(content_type):
		contentItem = content_type