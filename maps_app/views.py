from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required    
def india_map(request):
    return render(request,'test.html')

@login_required    
def puzzle(request):
    return render(request,'puzzle.html')
    
@login_required
def kt(request):
    return render(request,'kt.html')
