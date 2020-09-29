from django.db import models
from django.shortcuts import redirect,reverse
import django
# Create your models here.
class Note(models.Model):
    LABEL_CHOICES = (
        ('primary','primary'),
        ('success','success'),
        ('secondary','secondary'),
        ('danger','danger'),
        ('warning','warning'),
        ('info','info'),
        ('light','light'),
        ('dark','dark'),
    )
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField(default=django.utils.timezone.now)
    labels = models.CharField(max_length=50,choices=LABEL_CHOICES,default="success")
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title