from django.forms import ModelForm
from . import models

class TodoListForm(ModelForm):
    class Meta:
        model = models.Todo
        fields = ["title", "choice","content", "DueTime"]

# http://stackoverflow.com/questions/20875455/html-tags-for-choicefield-in-django
