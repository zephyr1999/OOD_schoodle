from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
    path("student/<int:student_id>", views.student_splash, name='student_splash'),
    path("instructor/<int:instructor_id>", views.instructor_splash, name='instructor_splash'),
    path("admin/<int:admin_id>", views.admin_splash, name='admin_splash'),
    path("addcourse/<int:admin_id>", views.add_course, name='add_course'),
    path("misc_content/<slug:content>", views.misc_content),
    path("course/<int:course_id>/studentview/<int:student_id>", views.studentview, name="studentview"),
    path("course/<int:course_id>/instructorview/<int:instructor_id>", views.instructorview, name="instructorview"),
    path("course/<int:course_id>/adminview/<int:admin_id>", views.adminview, name="adminview"),
    path("course/<int:course_id>/content/<int:content_id>", views.content, name="content"),
    path("course/<int:course_id>/studentgrades/<int:student_id>", views.studentgrades, name="studentgrades"),
    path("course/<int:course_id>/allgrades/<int:instructor_id>", views.allgrades, name="allgrades"),
    path("course/<int:course_id>/addcontent/<int:instructor_id>", views.add_content),
    path("course/<int:course_id>/addgrade/<int:instructor_id>/<int:student_id>", views.add_grade),
    path("course/<int:course_id>/addinstructor/<int:admin_id>",views.add_instructor),
    path("course/<int:course_id>/addstudent/<int:admin_id>",views.add_student),]

