from django.shortcuts import redirect, render, get_object_or_404

from main.models import Task


def home(request):
    tasks = Task.objects.filter(is_compeleted=False).order_by('updated')
    compeleted_task = Task.objects.filter(is_compeleted=True).order_by('updated')
    context = {
        'tasks' : tasks,
        'compeleted_task' : compeleted_task,
    }
    return render(request,'main/home.html',context)

def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_compeleted = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_compeleted = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            "get_task":get_task,
        }
        return render(request,'main/edit.html', context)
    
def delete_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    return redirect('home')