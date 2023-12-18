from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.hello,name='homepage'),
    path('add',views.add,name='add')
   
]
