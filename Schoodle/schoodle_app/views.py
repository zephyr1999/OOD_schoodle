from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Person,Course

def index(request):
    #default index view shows all people
    top_people = Person.objects.order_by('name')[:5]
    top_courses = Course.objects.order_by('name')[:5]
    template = loader.get_template('schoodle_app/index.html')
    context = {'top_people':top_people, 'top_courses':top_courses}
    return HttpResponse(template.render(context,request))

def person_detail(request,person_id):
    return HttpResponse("You're looking at person detail %s" % Person.objects.get(id=person_id))

def course_detail(request,course_id):
    return HttpResponse("You're looking at course detail %s" % Course.objects.get(id=course_id))
