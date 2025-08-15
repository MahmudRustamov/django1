from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return render(request, 'index.html')


def about_page_view(request):
    return render(request, 'about.html')


def teacher_page_view(request):
    return render(request, 'teacher.html')