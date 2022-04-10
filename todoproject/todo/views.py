from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import todomodel
from .forms import todoform

# Create your views here.

def todo(request):
    todo_list = todomodel.objects.order_by('id')
    form = todoform()
    context = {'todo_list' : todo_list, 'form' : form}
    return render(request, 'todo.html', context)

@require_POST
def addTodo(request):
    form = todoform(request.POST)
    if form.is_valid():
        new_todo = todomodel(text=request.POST['text'])
        new_todo.save()
    return redirect('todo')

def completeTodo(request, todo_id):
    todo = todomodel.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('todo')

def deleteCompleted(request):
    todomodel.objects.filter(complete__exact=True).delete()
    return redirect('todo')
