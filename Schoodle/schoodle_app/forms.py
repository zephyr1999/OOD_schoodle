from django import forms
from .models import *

class AddCourseForm(forms.Form):
    course_name = forms.CharField(label="New Course name", max_length=200)

class AddContentForm(forms.Form):
    description = forms.CharField(label="New Content", max_length=1000)

class AddGradeForm(forms.Form):
    grade = forms.FloatField(label="Grade")

