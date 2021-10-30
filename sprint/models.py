from django.db import models
from django.contrib.auth.models import User

class Sprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField(blank=True, default='')
    start = models.DateTimeField(unique=True)
    Duration= models.DurationField()
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or ('Sprint ending %s') % self.end