from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import Todo

from . import utils


def home(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")

    if request.method == 'GET':
        todos = Todo.objects.all().order_by('-created_at')

        for todo in todos:
            todo.priority = utils.get_todo_priority(todo)
            todo.done = 'Sim' if todo.done else 'Não'

        return render(request, 'home.html', {
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

        return redirect('/todo/home/')


def edit_todo(request, id):

    if not request.user.is_authenticated:
        return render(request, "login.html")

    if request.method == 'GET':
        todo = Todo.objects.get(id=id)

        return render(request, 'edit_todo.html', {
            'todo': todo,
        })

    title = request.POST.get('title')
    description = request.POST.get('description')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    done = request.POST.get('done')

    if len(title.strip()) < 2:
        return redirect(reverse('edit_todo', kwargs={'id': id}))

    if len(deadline) == 0:
        deadline = None

    todo = Todo.objects.get(id=id)
    todo.title = title
    todo.description = description
    todo.priority = priority
    todo.deadline = deadline
    todo.done = done
    todo.save()

    return redirect('/todo/home/')


def toggle_todo_done(request, id):
    if not request.user.is_authenticated:
        return render(request, "login.html")

    todo = Todo.objects.get(id=id)
    print(todo.done)
    todo.done = not todo.done
    print(todo.done)
    todo.save()

    return JsonResponse({
        'status': 'ok',
    })


def delete_todo(request, id):
    if not request.user.is_authenticated:
        return render(request, "login.html")

    todo = Todo.objects.filter(id=id)

    if todo.exists():
        todo.delete()

        return redirect('/todo/view_todo')
    else:
        return render(request, 'home.html')
