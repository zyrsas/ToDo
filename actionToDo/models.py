from django.db import models

# Create your models here.


class ToDoList(models.Model):
    id_ToDo = models.IntegerField(default=0)
    title = models.CharField(max_length=300, verbose_name="Title")
    deadline = models.CharField(max_length=50)
    priority = models.IntegerField()
    complete = models.BooleanField(default=False)
    date_of_modification = models.CharField(max_length=50, default="")

    class Meta:
        verbose_name_plural = "ToDo Lists"
        verbose_name = "ToDo List"

    def __str__(self):
        return self.title


class LastUpdate(models.Model):
    lastUpdate = models.CharField(max_length=50, default="")
