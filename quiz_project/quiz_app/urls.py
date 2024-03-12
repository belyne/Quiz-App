# quiz_app/urls.py
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('quiz/', views.quiz, name="quiz"),
]

