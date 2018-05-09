from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from actionToDo.models import ToDoList, LastUpdate

# Create your views here.


@api_view(['POST', ])
def CreateToDO(request):
    if request.method == "POST":
        try:
            if request.GET.get('title') and request.GET.get('deadline') and request.GET.get('priority'):
                new_todo = ToDoList(title=request.GET.get('title'), deadline=request.GET.get('deadline'), priority=request.GET.get('priority'))
                new_todo.save()

                json = ToDoList.objects.filter(id=new_todo.id).values('id',
                                                                      'title',
                                                                      'deadline',
                                                                      'priority',
                                                                      'complete')
                return Response({"status": True, "data": json})
            else:
                return Response({"Result": False, "data": []})

        except KeyError:
            return Response({"Result": False, "data": []})
        except ValueError:
            return Response({"Result": False, "data": []})
        except:
            return Response({"Result": False, "data": []})


@api_view(['POST', ])
def MarkCompleteToDo(request):
    if request.method == "POST":
        try:
            if request.GET.get('id'):
                todo = ToDoList.objects.filter(id=request.GET.get('id'))
                for item in todo:
                    item.complete = True
                    item.save()


                json = ToDoList.objects.filter(id=request.GET.get('id')).values(
                                                                  'id',
                                                                  'title',
                                                                  'deadline',
                                                                  'priority',
                                                                  'complete')
                return Response({"status": True, "data": json})
            else:
                return Response({"Result": False, "data": []})

        except KeyError:
            return Response({"Result": False, "data": []})
        except ValueError:
            return Response({"Result": False, "data": []})
        except:
            return Response({"Result": False, "data": []})
