from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.views.generic.list import ListView
from .import models
import datetime
from django.utils.timezone import now
from django.contrib import auth


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/todo/")
        else:
            # Show an error page
            return HttpResponseRedirect("/todo/login_view/")
    today = datetime.date.today()
    return render(request, 'taskbuster/index.html', {"today":today, "now":now() })

def todo(request):
    present_form = forms.TodoListForm(request.POST or None)
    if present_form.is_valid():
        instance = present_form.save()
        request.session['has_new']=True
        return HttpResponseRedirect('/todo/')

    return render(request, 'taskbuster/todo.html', {'present_form':present_form})


def display(request):
    if request.user.is_authenticated():
        queryset=models.Todo.objects.all().order_by("choice")

        return render(request, "taskbuster/display.html", {"queryset":queryset})

    else:
        if request.session.get('has_new', False):
            return HttpResponse("You did it!")
        else:
            return HttpResponse("You are not authorizated")


def deleteSession(request):
    try:
        del request.session['has_new']
    except KeyError:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/todo/')

def delete(request, id=None):
    instance = get_object_or_404(models.Todo, id=id)
    instance.delete()
    return HttpResponseRedirect('/todo/')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'taskbuster/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/todo/")
        else:
            # Show an error page
            return HttpResponseRedirect("/todo/login_view/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")
