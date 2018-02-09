from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentsListView.as_view(), name='students'),
    path('student/<int:pk>/', views.StudentListView.as_view(), name='student'),
]