# this file needs references to all classes in the subdirecorty
# From Django documentation and a class named "Book" in a file called book.py
# This would look like: from .book import Book
from .person import Person
from .course import Course
from .administrator import Administrator
from .contentItem import ContentItem
from .contentItemFactory import ContentItemFactory
from .contentitemcollection import ContentItemCollection
from .course_collection import CourseCollection
from .fileItem import FileItem
from .grade import Grade
from .gradesCollection import GradesCollection
from .instructor import Instructor
from .newsItem import NewsItem
from .question import Question
from .quiz import Quiz
#from .student import Student

