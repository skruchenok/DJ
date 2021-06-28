from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from core.models import ToDo
from core.forms import SignUpForm, TodoCreationForm


def hello(request):
    # return HttpResponse('<b>HELLO WORLD!</b>')
    return render(request, 'base.html')


@login_required
def todos(request):
    user = request.user
    todos_list = ToDo.objects.filter(user=user)
    return render(request, 'index.html', context={"todos_list": todos_list})


class TodoListView(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    template_name = 'create_todo.html'
    form_class = TodoCreationForm
    success_url = '/todos/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserRegistrationView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user=user)
        return redirect('hello')
    return render(request, 'login.html')
