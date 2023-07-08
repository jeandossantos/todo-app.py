from django.shortcuts import render, redirect

from .models import Todo

from . import utils


def view_todo(request):
    if request.method == 'GET':
        todos = Todo.objects.all().order_by('-created_at')

        for todo in todos:
            todo.priority = utils.get_todo_priority(todo)
            todo.done = 'Sim' if todo.done else 'Não'

        return render(request, 'view_todo.html', {
            'todos': todos
        })
    elif request.method == 'POST':
        user_id = request.session.get('user_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        deadline = request.POST.get('deadline')
        done = request.POST.get('done')

        if len(deadline) == 0:
            deadline = None

        todo = Todo(title=title, description=description,
                    priority=priority, deadline=deadline, done=done, user_id=user_id)

        todo.save()

        return redirect('/todo/view_todo/')


def delete_todo(request, id):
    todo = Todo.objects.filter(id=id)

    if todo.exists():
        todo.delete()

        return redirect('/todo/view_todo')
    else:
        return render(request, 'view_todo.html')
