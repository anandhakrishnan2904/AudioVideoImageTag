from django.urls import path,include
from . import views
urlpatterns = [
   
path('', views.imageaudiovideo, name='imageaudiovideo'), 


]
