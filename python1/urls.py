from django.urls import path
from .views import main,content,rais,rain
urlpatterns = [
    path('',main,name="home"),
    path('content/',content,name='content'),
    path('rain/',rain,name='rain'),
    path('rais/',rais,name='rais'),
]
