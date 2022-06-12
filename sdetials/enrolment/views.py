from tkinter.messagebox import NO
from tokenize import Name
from turtle import title
from django.shortcuts import render
from .forms import searchF, stude
from .models import student


# Create your views here.


def showw(request):
    return render(request, "base.html")


def show(request):
    return render(request, "home.html")


def register(request):
    form = stude(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Name']
        enrollment = form.cleaned_data['enrollment_no']
        p = student(Name=name, enrollment_no=enrollment)
        p.save()
        return render(request, "success.html", {"title": "registration succcesfully"})

    return render(request, "register.html", {'form': form})


def done(request):
    title = " all student"
    queryset = student.objects.all()

    context = {
        "title": title,
        "queryset": queryset,

    }
    return render(request, "done.html", context)


def search(request):
    title = " search student"
    form = searchF(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['Name']
        queryset = student.objects.filter(Name=name)
        context = {
            "title": title,
            'queryset': queryset
        }
        return render(request, "done.html", context)

    context = {
        "title": title,
        'form': form,
    }
    return render(request, "search.html", context)
