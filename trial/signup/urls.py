from django.urls import path
from . import views

urlpatterns=[path("signup/",views.signupform1,name="signup"),

]