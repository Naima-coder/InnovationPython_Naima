from django.shortcuts import render,get_object_or_404,redirect
from .models import modelclass
from .form import blogform
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def list(request):
    fields = modelclass.objects.all()
    arg={"fields":fields}
    return render(request,"BLOG_POSTS/homepage.html", arg)
def about(request):
    return render(request,"BLOG_POSTS/about.html")

def add(request):
    form=blogform(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,"BLOG_POSTS/homepage.html")
    else:
        form=blogform()
        context={"form":form}
    return render(request, "BLOG_POSTS/POST_FORM.html",context)
def blog_delete(request,pk):
    data=get_object_or_404(modelclass,pk=pk)
    if request.method=="POST":
        data.delete()
        return render(request,"BLOG_POSTS/homepage.html")
    return render(request,"BLOG_POSTS/POST_DELETE.html")
def login(request):
    if request.method=="POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"BLOG_POSTS/homepage.html")
        else:
            messages.info(request, "Invalid credentials ")
            return render(request,"log/login.html")

    else:
        return render(request,"log/login.html")
def register(request):
    if request.method == "POST":
        username = request.POST['Username']
        first_name = request.POST['First name']
        last_name = request.POST['Last name']
        password= request.POST['Password']
        password_2 = request.POST['Password2']
        if password==password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username has been taken!!")
                return render(request,"sign/signup.html")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password, )
                user.save()
                messages.info(request,"User created! ")
                return render(request,"log/login.html")
    else:
        return render(request, "sign/signup.html")
def home(request):
    return render(request,"home.html")
def logout(request):
    auth.logout(request)
    return redirect("/")
def test(request):
    return render(request,"BLOG_POSTS/homepage.html")





