from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')   


def teacher(request):
    return render(request,'teacher.html')
def sp_teacher(request):
    return render(request,'sp_teacher.html')