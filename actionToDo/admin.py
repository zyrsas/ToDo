from django.contrib import admin
from actionToDo.models import ToDoList, LastUpdate

# Register your models here.

admin.site.register(ToDoList)
admin.site.register(LastUpdate)
