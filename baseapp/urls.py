from django.urls import path

from . import views

urlpatterns = [
    path('', views.BaseAppListView.as_view(), name='home'),
]