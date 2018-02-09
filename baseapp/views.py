# blog/views.py
from django.views.generic import ListView
from . models import UserAccounts

class BaseAppListView(ListView):
    model = UserAccounts
    template_name = 'home.html'