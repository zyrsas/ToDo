from django.db import models
from django_unixdatetimefield import UnixDateTimeField

# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    deadline = models.CharField(max_length=30)
    priority = models.IntegerField()
    complete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Title"
        verbose_name = "Title"

    def __str__(self):
        return self.title


class LastUpdate(models.Model):
    update = UnixDateTimeField()
