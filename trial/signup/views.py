from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

# Create your views here.

def signupform1(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            form=UserCreationForm()
            return redirect("/loginapp/login")
    else:
        form=UserCreationForm()

    return render(request,"signup/signup.html",{'signup_form':form})

