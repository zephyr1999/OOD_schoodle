from django.db import models
from .contentItem import ContentItem

class ContentItemCollection(models.Model):
	# data members
	contentItemList = models.OneToMany(ContentItem)

	def addItem(ci):
		contentItemList.append(ci)

	def deleteItem(ci):
		contentItemList.remove(ci)