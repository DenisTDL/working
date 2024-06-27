from django.shortcuts import render


def one(request):
    return render(request, 'mysit/one.html')


def two(request):
    return render(request, 'mysit/two.html')


def three(request):
    return render(request, 'mysit/three.html')
