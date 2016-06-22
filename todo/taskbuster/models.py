from django.db import models
from datetime import date

class Todo(models.Model):
    level = (
        (0, 'relax'),
        (1, 'emergent'),
        (2, 'superb')
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    choice = models.SmallIntegerField( choices=level)
    DueTime = models.DateField(default=date.today) # auto_now_add=True
    def __str__(self):
        return self.title
