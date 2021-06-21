from core.models import User
from django.urls import path

from core.views import hello, todos, UserRegistrationView

urlpatterns = [
    path('', hello),
    path('todos/', todos),
    path('signup/', UserRegistrationView.as_view()),
    path('login/', )
]
