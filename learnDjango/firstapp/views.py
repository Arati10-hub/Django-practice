from django.shortcuts import render,HttpResponse
#Suppose we create class A()
# Create your views here.
#function baesd view

def about(request):
    return HttpResponse("About page")

def home(main):
    return HttpResponse("Main page")

def addcart(items):
    return HttpResponse("Add items")

def contact(help):
    return HttpResponse("Contact us")

def courses(request):
    return render(request,"courses.html",{})

def fees(request):
    return render(request,"fees.html",{})

def teacher(request):
    return render(request,"teacher.html",{})

