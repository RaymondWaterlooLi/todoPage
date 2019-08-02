from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoItem

# Create your views here.

def todoView (request):
    all_todo_items = todoItem.objects.all()
    return render(request, 'todo.html',{'all_items': all_todo_items})


def addTodo(request):
    new_item = todoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = todoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

