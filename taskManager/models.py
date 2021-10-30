from django.db import models
from django.contrib.auth.models import User
from sprint.models import Sprint


# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = (
        ('Todo', 'Todo'),
    ('Progress', 'Progress'),
    ('Review', 'Review'),
    ('Done', 'Done'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    projectname = models.CharField(max_length=200, default="")
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)   
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    subtask = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

