from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import AuthenticationForm

def login_form(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            context={"succ":"succ"}
            return render(request,"login/success.html",context)
    else:
        form = AuthenticationForm()
    return render(request, "login/login.html", {"login_c":form})





