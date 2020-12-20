from django.urls import path
from . import views
urlpatterns=[path("list/",views.list,name="view1"),
             path("add/",views.add,name="view2"),
             path('delete/<int:pk>',views.blog_delete,name="view3"),
             ]