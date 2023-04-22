from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm

# Create your views here.

def homePage(request):
    tasks = Tasks.objects.all()

    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def updatePage(request, pk):
    tasks = Tasks.objects.get(id=pk)

    form = TasksForm(instance=tasks)

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/update.html', context)

def deletePage(request, pk):
    item = Tasks.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'base/delete.html', context)