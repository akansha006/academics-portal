# blog/views.py
from django.views.generic import ListView
from . models import Students,Marks

class StudentsListView(ListView):
    model = Students
    template_name = 'students.html'

class StudentListView(ListView):
    model = Marks
    template_name = 'student.html'