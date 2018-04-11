from django.db import models

class Question():
	#data members
	questionText = models.CharField(max_length=1000)
	answer = models.CharField(max_length=500)
	answerTextList = models.OneToMany(answer)
	correctAnswerIndex = models.IntegerField(default=0)

	def isCorrect(choice):
		if choice == correctAnswerIndex:
			return True
		else:
			return False