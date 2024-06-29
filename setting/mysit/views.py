from django.shortcuts import render
from .models import Task

def one(request):
    x = Task.objects.all()
    return render(request, 'mysit/one.html', {"x": x})


def two(request):
    return render(request, 'mysit/two.html')


def three(request):
    return render(request, 'mysit/three.html')


def create(request):
    return render(request, 'mysit/create.html')
