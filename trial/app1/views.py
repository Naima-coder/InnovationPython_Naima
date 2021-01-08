from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import form1,mform

# Create your views here.
def basic(request):
    return HttpResponse(" THIS IS THE BASIC HARD CODE VIEW ")
def view1(request):
    context={"tag_var":"tag_var"}
    return render(request,"htmlview.html",context)
def result(request):

        val1 = int(request.POST["num1"])
        val2 = int(request.POST["num2"])
        res = val1 + val2
        return render(request,"result.html",{"result":res})


def view2(request):
    form = form1()
    context={'form':form}
    return render(request,"htmlview.html",context)
def view3(request):
    form=mform(request.POST or None)
    if form.is_valid():
        form.save()
        form = mform()
    context={"form1":form}
    return render(request,"newhtml.html",context)