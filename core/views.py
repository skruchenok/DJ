from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import CreateView

from core.models import ToDo
from core.forms import SignUpForm


def hello(request):
    return HttpResponse('<b>HELLO WORLD!</b>')

def todos(request):
    todos_list = ToDo.objects.all()
    return render(request, 'index.html', context={"todos_list": todos_list})


class UserRegistrationView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
