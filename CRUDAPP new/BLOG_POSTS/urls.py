from django.urls import path
from . import views
urlpatterns=[path("list/",views.list,name="view1"),
             path("add/",views.add,name="view2"),
             path('delete/<int:pk>',views.blog_delete,name="view3"),
             path("log",views.login,name="login"),
             path("reg",views.register,name="regi"),
             path("",views.home,name="home"),
             path("home",views.test,name="homepage"),
             path("logout",views.logout,name="logout"),
             path("about",views.about,name="about"),
             path("test",views.test,name="test")

             ]