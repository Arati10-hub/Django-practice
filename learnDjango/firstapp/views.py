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

def students(request):
    print("________________________________________")
    print(request.method)
    print("________________________________________")
    context={"id":101,"name":"Aish","subjects":["html","CSS","Js"]}
    return render(request,"students.html",context)


def book(request):
    print(request.GET.get("bookname"))
    print(request.GET.get("price"))
    context={"bookname":request.GET.get("bookname"),
             "price":request.GET.get("price")}
    return render(request,"book.html",context)

def product(request):
    print(request.GET.get("productname"))
    print(request.GET.get("price"))
    context={"name":request.GET.get("productname"),
             "price":request.GET.get("price")}
    return render(request,"product.html",context)


def employee(request):
    context={"id":101,"name":"arti","dept":"IT","skills":["python","sql","html","CSS","Js"]}
    return render(request,"employee.html",context)

def customer(request):
    return render(request,"customer.html")