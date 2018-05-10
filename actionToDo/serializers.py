from rest_framework import serializers
from actionToDo.models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id_ToDo', 'title', 'deadline', 'priority', 'complete', 'date_of_modification')
