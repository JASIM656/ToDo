from django.shortcuts import render,redirect
from .models import Task
def index(request):
    task=Task.objects.all()
    if request.method == 'POST':
        a = request.POST.get('item')
        b = request.POST.get('description')
        c = request.POST.get('priority')
        Task.objects.create(name=a , description=b, priority=c)
        return redirect('index')
    return render(request,'index.html',{'task':task})


# Create your views here.


