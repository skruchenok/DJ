from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from core.views import hello, todos, my_login, UserRegistrationView

urlpatterns = [
    path('', hello, name='hello'),
    path('todos/', todos, name='todos'),
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
