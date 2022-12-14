from django.shortcuts import render, HttpResponse
from home import models

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method=="post":
        print("this is post")
        name=request.Post['name']
        phone=request.Post['phone']
        email=request.Post['email']
        print(name,phone,email)
        ins=contact(name=name,email=email,phone=phone)
        ins.save()
        print("the data has been written to the db")
    return render(request,'contact.html')


