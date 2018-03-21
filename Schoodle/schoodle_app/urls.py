from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path("person/<int:person_id>", views.person_detail, name='person_detail'),
               path("course/<int:course_id>", views.course_detail, name='course_detail')]
