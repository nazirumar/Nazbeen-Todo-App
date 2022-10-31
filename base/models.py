from email.policy import default
from turtle import title
from django.db import models

# Create your models here.


class TodoApp(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateField()
    updated= models.DateTimeField(auto_now_add=True)
    is_reading = models.BooleanField(default=True)



    def __str__(self):
        return self.title


    class Meta:
        db_table = 'todo_app'
        ordering = ['-created']

