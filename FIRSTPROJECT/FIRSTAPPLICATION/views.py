from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
    return HttpResponse(" Hey..,This is the first view using HttpResponce!")
def view2(request):
    context={"tag_var":"tag_var"}
    return render(request,"new.html",context)
# Create your views here.
