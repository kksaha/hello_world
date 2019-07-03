from django.urls import path
from .views import UserView

app_name = "user"

urlpatterns = [
    path('hello/<str:user_name>/', UserView.as_view()),
]
