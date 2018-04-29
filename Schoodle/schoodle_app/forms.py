from django import forms
from .models import *

class AddCourseForm(forms.Form):
    course_name = forms.CharField(label="New Course name", max_length=200)

class AddContentForm(forms.Form):
    description = forms.CharField(label="New Content", max_length=1000)

class AddGradeForm(forms.Form):
    grade = forms.FloatField(label="Grade")

class AddInstructorForm(forms.Form):
    instructor = forms.ModelChoiceField(queryset=None)
    def __init__(self,course_id,*args, **kwargs):
        super().__init__(*args, **kwargs)
        #course_id=kwargs.get('course_id')
        course= Course.objects.get(id=course_id)
        courseInstructors = Instructor.objects.filter(id__in=[p.id for p in course.person_set.all()])
        self.fields['instructor'].queryset = Instructor.objects.all().exclude(id__in=[i.id for i in courseInstructors])

class AddStudentForm(forms.Form):
    student = forms.ModelChoiceField(queryset=None)
    def __init__(self,course_id,*args, **kwargs):
        super().__init__(*args, **kwargs)
        #course_id=kwargs.get('course_id')
        course= Course.objects.get(id=course_id)
        courseStudents = Student.objects.filter(id__in=[p.id for p in course.person_set.all()])
        self.fields['student'].queryset = Student.objects.all().exclude(id__in=[i.id for i in courseStudents])


