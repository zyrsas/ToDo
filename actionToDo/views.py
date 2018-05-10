from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from actionToDo.models import ToDoList, LastUpdate
from actionToDo.serializers import ToDoListSerializer

# Create your views here.


@api_view(['POST', ])
def CreateToDO(request):
    if request.method == "POST":
        try:
            if request.GET.get('id') and request.GET.get('complete') and request.GET.get('title') and request.GET.get('deadline') and request.GET.get('priority') and request.GET.get('date'):
                new_todo = ToDoList(title=request.GET.get('title'),
                                    id_ToDo=request.GET.get('id'),
                                    complete=request.GET.get('complete'),
                                    deadline=request.GET.get('deadline'),
                                    priority=request.GET.get('priority'),
                                    date_of_modification=request.GET.get('date'))
                new_todo.save()

                json = ToDoList.objects.filter(id_ToDo=new_todo.id_ToDo).values(
                                                                      'id_ToDo',
                                                                      'title',
                                                                      'deadline',
                                                                      'priority',
                                                                      'complete',
                                                                      'date_of_modification')
                return Response({"status": True, "data": json})
            else:
                return Response({"status": False, "data": []})

        except KeyError:
            return Response({"status": False, "data": []})
        except ValueError:
            return Response({"status": False, "data": []})
        except:
            return Response({"status": False, "data": []})


@api_view(['POST', ])
def MarkCompleteToDo(request):
    if request.method == "POST":
        try:
            if request.GET.get('id'):
                todo = ToDoList.objects.filter(id_ToDo=request.GET.get('id'))
                for item in todo:
                    item.complete = True
                    item.save()


                json = ToDoList.objects.filter(id_ToDo=request.GET.get('id')).values(
                                                                  'id_ToDo',
                                                                  'title',
                                                                  'deadline',
                                                                  'priority',
                                                                  'complete',
                                                                  'date_of_modification')
                return Response({"status": True, "data": json})
            else:
                return Response({"status": False, "data": []})

        except KeyError:
            return Response({"status": False, "data": []})
        except ValueError:
            return Response({"status": False, "data": []})
        except:
            return Response({"status": False, "data": []})


@api_view(['POST', ])
def EditToDo(request):
    if request.method == "POST":
        try:
            if request.GET.get('id') and request.GET.get('complete') and request.GET.get('title') and request.GET.get('deadline') and request.GET.get('priority') and request.GET.get('date'):
                todo = ToDoList.objects.filter(id_ToDo=request.GET.get('id'))
                for item in todo:
                    item.complete = request.GET.get('complete')
                    item.title = request.GET.get('title')
                    item.deadline = request.GET.get('deadline')
                    item.priority = request.GET.get('priority')
                    item.date_of_modification = request.GET.get('date')
                    item.save()


                json = ToDoList.objects.filter(id_ToDo=request.GET.get('id')).values(
                                                                  'id_ToDo',
                                                                  'title',
                                                                  'deadline',
                                                                  'priority',
                                                                  'complete',
                                                                  'date_of_modification')
                return Response({"status": True, "data": json})
            else:
                return Response({"status": False, "data": []})

        except KeyError:
            return Response({"status": False, "data": []})
        except ValueError:
            return Response({"status": False, "data": []})
        except:
            return Response({"status": False, "data": []})


@api_view(['POST', ])
def GetLastUpdate(request):
    if request.method == "POST":
        try:
            if LastUpdate.objects.filter(id=0).count > 0:
                update = LastUpdate.objects.filter(id=0)

                json = LastUpdate.objects.filter(id=0).values(
                                                                  'lastUpdate',
                                                               )
                return Response({"status": True, "data": json})
            else:
                return Response({"status": False, "data": []})

        except KeyError:
            return Response({"status": False, "data": []})
        except ValueError:
            return Response({"status": False, "data": []})
        except:
            return Response({"status": False, "data": []})


@api_view(['POST', ])
def GetLastUpdate(request):
    if request.method == "POST":
        try:
            if LastUpdate.objects.filter(id=0).count > 0:
                update = LastUpdate.objects.filter(id=0)

                json = LastUpdate.objects.filter(id=0).values(
                                                                  'lastUpdate',
                                                               )
                return Response({"status": True, "data": json})
            else:
                return Response({"status": False, "data": []})

        except KeyError:
            return Response({"status": False, "data": []})
        except ValueError:
            return Response({"status": False, "data": []})
        except:
            return Response({"status": False, "data": []})


@api_view(['POST', ])
def SetLastUpdate(request):
    if request.method == "POST":
        try:
            if request.GET.get('date'):
                if LastUpdate.objects.count() > 0:
                    update = LastUpdate.objects.filter(id=1)
                    for item in update:
                        item.lastUpdate = request.GET.get('date')
                        item.save()
                    json = LastUpdate.objects.filter(id=1).values(
                                                                  'lastUpdate',
                                                               )
                    return Response({"status": True, "data": json})
                else:
                    update = LastUpdate(lastUpdate=request.GET.get('date'))
                    update.save()
                    json = LastUpdate.objects.filter(id=1).values(
                        'lastUpdate',
                    )
                    return Response({"status": True, "data": json})
            else:
                Response({"status": False, "data": []})

        except KeyError:
            return Response({"status": False, "data": []})
        except ValueError:
            return Response({"status": False, "data": []})
        except:
            return Response({"status": False, "data": []})


class ToDoLists(generics.ListCreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer