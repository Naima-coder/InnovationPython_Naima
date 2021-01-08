
from django.urls import path
from . import views
urlpatterns=[path("a/",views.basic,name="basic"),
             path("",views.view1,name="view1"),
             path("f/",views.view2,name="view2"),
             path("nf/",views.view3,name="view3"),
             path("add",views.result,name="resultadd"),

]