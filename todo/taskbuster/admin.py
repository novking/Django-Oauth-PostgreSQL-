from django.contrib import admin
from . import models

class TodoModel(admin.ModelAdmin):
    list_display = ["title", "choice", "DueTime"]
    list_display_links = ["title"]
    class Meta:
        model = models.Todo


admin.site.register(models.Todo, TodoModel)
