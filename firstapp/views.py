from django.shortcuts import render

# Create your views here.
def djafun(request):
    return render(request,'hello.html')
def link(request):
    return render(request,'hello2.html')
def link2(request):
    return render(request,'hello3.html')
def link3(request):
    return render(request,'hello4.html')
def ktm(request):
    return render(request,'kottayam.html')
def wyd(request):
    return render(request,'wayanad.html')
def ekm(request):
    return render(request,'ernakulam.html')
def back(request):
    return render(request,'hello.html')

