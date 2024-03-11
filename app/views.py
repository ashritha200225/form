from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def index(request):
    form=my_form()
    if request.method == 'POST':
       fm=my_form(request.POST)
       if fm.is_valid():
           return  HttpResponse("data is valid")
       else:
           return  HttpResponse("data invalid")

    return render(request,'index.html',{'form':form})        