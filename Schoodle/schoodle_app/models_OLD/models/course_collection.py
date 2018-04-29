from django import models
from .course import Course

class CourseCollection(models.Model):
    # all collections contain a list
    courses = models.ManyToManyField(Course)

    def addCourse(self,c):
        # c is a new course object
        self.courses.add(c)
        self.save()

    def getCourse(self, _id):
        return self.courses.filter(id=_id)

    def deleteCourse(self, c):
        self.courses.remove(c)
        self.save()
