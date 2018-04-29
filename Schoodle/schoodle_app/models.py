from django.db import models

class Course(models.Model):
    #data members
    name = models.CharField(max_length=200)
    # This definition actually means one person has many courses
    #persons = models.ManyToManyField(Person)
    #students = models.ManyToManyField(Student)
    #instructors = models.ManyToManyField(Instructor)
    #quizzes = models.ManyToManyField(Quiz)

    #class functions
    def __str__(self):
        #default tostring
        return self.name

    def get_ID(self):
        return self.id


class Person(models.Model):
    # data members
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)

    # functions
    def __str__(self):
        #default tostring method
        return self.name

    def get_ID(self):
        return self.id

class Grade(models.Model):
    g = models.FloatField()

class ContentItem(models.Model):
        #data members
        grade = models.FloatField(default=0.0)
        description = models.CharField(max_length=1000)
        associatedCourse = models.ForeignKey(Course, on_delete=models.CASCADE)

        def setGrade(gradeInput):
                self.grade = gradeInput

        def getGrade():
                return self.grade

class ContentItemCollection(models.Model):
        # data members
        contentItemList = models.ForeignKey(ContentItem, on_delete=models.CASCADE)

        def addItem(ci):
                contentItemList.append(ci)

        def deleteItem(ci):
                contentItemList.remove(ci)



class Student(Person):
    grades = models.ManyToManyField(Grade)
    content = models.OneToOneField(ContentItemCollection,on_delete=models.CASCADE)


class Administrator(Person):
    # admin has no attributes beyond person
    # but has several course managment style methods

    def add_student(self,s,c):
        #add student s to course c
        c.students.add(s)
        c.save()

    def add_instructor(self,i,c):
        #add instructor i to course c
        c.instructors.add(i)
        c.save()

    def remove_student(self,s,c):
        #remove s from c
        c.students.remove(s)
        c.save()

    def remove_instructor(self,i,c):
        #remove i from c
        c.instructors.remove(i)

class ContentItemFactory(models.Model):
        contentItem = models.CharField(max_length=200)

        def createContent(content_type):
                contentItem = content_type


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

class FileItem(models.Model):
        # data members
        contentPath = models.CharField(max_length=200)

        def __str__(self):
                #default tostring
                return self.contentPath

class GradesCollection(models.Model):
        #data members
        gradesList = models.ForeignKey(Grade, on_delete=models.CASCADE)

        def addGrade(g):
                gradesList.append(g)

        def getGrade(g):
                for grade in gradesList:
                        if grade == g:
                                return grade


class Instructor(Person):
    #instructor only has one additional field to person base class
    content = models.OneToOneField(ContentItemCollection,on_delete=models.CASCADE)

class NewsItem(models.Model):
        # data members
        news = models.CharField(max_length=200)

        def __str__(self):
                #default tostring
                return self.news

  
class Question(models.Model):
        #data members
        questionText = models.CharField(max_length=1000)
        answer = models.CharField(max_length=500)
        #answerTextList = models.OneToMany(answer)
        correctAnswerIndex = models.IntegerField(default=0)

        def isCorrect(choice):
                if choice == correctAnswerIndex:
                        return True
                else:
                        return False


class Question(models.Model):
    # data members
    questionText = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)

