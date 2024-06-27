from django.urls import path
from . import views


urlpatterns = [
    path('', views.one, name='1'),
    path('two', views.two, name='2'),
    path('three', views.three, name='3'),
]
