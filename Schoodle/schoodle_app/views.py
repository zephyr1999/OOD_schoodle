from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *
from .forms import *

def index(request):
    #default index view shows all people
    students = Student.objects.all()
    instructors = Instructor.objects.all()
    admins = Administrator.objects.all()
    template = loader.get_template('schoodle_app/index.html')
    context = {"students":students,"instructors":instructors,"admins":admins}
    return HttpResponse(template.render(context,request))

def student_splash(request,student_id):
    courses = Student.objects.get(id=student_id).courses.all()
    template = loader.get_template('schoodle_app/student_splash.html')
    context = {"courses":courses,"student_id":student_id}
    return HttpResponse(template.render(context,request))

def instructor_splash(request,instructor_id):
    courses = Instructor.objects.get(id=instructor_id).courses.all()
    template = loader.get_template('schoodle_app/instructor_splash.html')
    context = {"courses":courses,"instructor_id":instructor_id}
    return HttpResponse(template.render(context,request))


def admin_splash(request,admin_id):
    courses = Administrator.objects.get(id=admin_id).courses.all()
    template = loader.get_template('schoodle_app/admin_splash.html')
    context = {"courses":courses,"admin_id":admin_id}
    return HttpResponse(template.render(context,request))

def add_course(request,admin_id):
    if request.method =="POST":
        f = AddCourseForm(request.POST)
        if f.is_valid():
            # make new course object and show success screen
            c = Course(name=f.cleaned_data['course_name'])
            c.save()
            #add to admin's list
            i=Administrator.objects.get(id=admin_id)
            i.courses.add(c)
            i.save()
            template = loader.get_template('schoodle_app/add_course_success.html')
            context = {"course":c,"admin_id":admin_id}
            return HttpResponse(template.render(context,request))
    else:
        f = AddCourseForm()
        return render(request, 'schoodle_app/add_course.html', {"form":f})

def add_content(request,course_id,instructor_id):
    if request.method =="POST":
        f = AddContentForm(request.POST)
        if f.is_valid():
            # make new content object and show success screen
            c = Course.objects.get(id=course_id)
            content = ContentItem(description=f.cleaned_data['description'],associatedCourse=c)
            content.save()
            #add to admin's list
            template = loader.get_template('schoodle_app/add_content_success.html')
            context = {"course":c, "content":content,"instructor_id":instructor_id}
            return HttpResponse(template.render(context,request))
    else:
        f = AddContentForm()
        return render(request, 'schoodle_app/add_content.html', {"form":f})

def add_grade(request,course_id,instructor_id,student_id):
    if request.method =="POST":
        f = AddGradeForm(request.POST)
        if f.is_valid():
            # make new grade object and show success screen
            grade = Grade(g=f.cleaned_data['grade'])
            grade.save()
            s = Student.objects.get(id=student_id)
            s.grades.add(grade)
            s.save()
            template = loader.get_template('schoodle_app/add_grade_success.html')
            context = {"course":Course.objects.get(id=course_id),"student":s,"instructor_id":instructor_id}
            return HttpResponse(template.render(context,request))
    else:
        f = AddGradeForm()
        return render(request, 'schoodle_app/add_grade.html', {"form":f})




def misc_content(request,content):
    # method for handling unimplimented views
    return HttpResponse("<h1>Schoodle App</h1><hr>" + content + " would appear in this view. Implimenting things like syllabus and assignments was outside the scope of our project.")

def studentview(request,course_id,student_id):
    course = Course.objects.get(id=course_id)
    items = course.contentitem_set.all()
    template = loader.get_template('schoodle_app/course_student.html')
    context = {"c":course,"items":items,"student_id":student_id}
    return HttpResponse(template.render(context,request))

def instructorview(request,course_id,instructor_id):
    course = Course.objects.get(id=course_id)
    items = course.contentitem_set.all()
    template = loader.get_template('schoodle_app/course_instructor.html')
    context = {"c":course,"items":items,"instructor_id":instructor_id}
    return HttpResponse(template.render(context,request))

def adminview(request,course_id,admin_id):
    course = Course.objects.get(id=course_id)
    items = course.contentitem_set.all()
    template = loader.get_template('schoodle_app/course_admin.html')
    context = {"c":course,"items":items,"admin_id":admin_id}
    return HttpResponse(template.render(context,request))

def content(request,course_id,content_id):
    return HttpResponse('<h1>Schoodle App</h1><hr> <h3>'+Course.objects.get(id=course_id).name+'</h3><hr> <p>' + ContentItem.objects.get(id=content_id).description+'</p>')

def studentgrades(request,course_id,student_id):
    grades = Student.objects.get(id=student_id).grades.all()
    course = Course.objects.get(id=course_id)
    template = loader.get_template('schoodle_app/studentgrades.html')
    context = {"c":course,"grades":grades}
    return HttpResponse(template.render(context,request))

def allgrades(request,course_id,instructor_id):
    course = Course.objects.get(id=course_id)   
    #students = course.person_set.all().filter(id__in=[s.id for s in Student.objects.all()])
    students = Student.objects.filter(id__in=[p.id for p in course.person_set.all()])
    template = loader.get_template('schoodle_app/allgrades.html')
    context = {"c":course,"students":students,"instructor_id":instructor_id}
    return HttpResponse(template.render(context,request))







