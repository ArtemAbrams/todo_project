from django.shortcuts import render
from todo.models.models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def task_list(request):
    user = request.user

    tasks = Task.objects.filter(user=user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(title=title, description=description, user=request.user)
        return redirect('task_list')
    return render(request, 'add_task.html')