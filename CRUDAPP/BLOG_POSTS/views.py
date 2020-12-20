from django.shortcuts import render,get_object_or_404
from django import forms
from .models import modelclass
from django.views.generic import FormView
# Create your views here.
class blogform(forms.ModelForm):
    class Meta:
        model=modelclass
        fields="__all__"
def list(request):
    data=modelclass.objects.all()
    context={"list":data}
    return render(request,"BLOG_POSTS/POST_LIST.html",context)
def add(request):
    form=blogform(request.POST or None)
    if form.is_valid():
        form.save()
        data=modelclass.objects.all()
        context={"list":data}
        return render(request,"BLOG_POSTS/POST_LIST.html",context)
    return render(request,"BLOG_POSTS/POST_FORM.html",{"form":form})
def blog_delete(request,pk):
    data=get_object_or_404(modelclass,pk=pk)
    if request.method=="POST":
        data.delete()
        context={"list":data}
        return render(request,"BLOG_POSTS/POST_LIST.html",context)
    return render(request,"BLOG_POSTS/POST_DELETE.html",{"delete":data})





