from django.contrib import path
from .import views

urlpatterns = [
     path('',views.index),
     path('about-as',views.about),
]