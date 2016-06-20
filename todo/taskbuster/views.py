from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.views.generic.list import ListView
from .import models

def index(request):
    return render(request, 'taskbuster/index.html')

def todo(request):
    present_form = forms.TodoListForm(request.POST or None)
    if present_form.is_valid():
        instance = present_form.save()
        return HttpResponseRedirect('/todo/')

    return render(request, 'taskbuster/todo.html', {'present_form':present_form})


def display(request):
    queryset=models.Todo.objects.all().order_by("choice")

    return render(request, "taskbuster/display.html", {"queryset":queryset})

def delete(request, id=None):
    instance = get_object_or_404(models.Todo, id=id)
    instance.delete()
    return HttpResponseRedirect('/todo/')
