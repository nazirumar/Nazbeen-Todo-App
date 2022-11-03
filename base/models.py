from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class TodoApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateField()
    updated= models.DateTimeField(auto_now_add=True)
    is_reading = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    class Meta:
        order_with_respect_to = 'user'


