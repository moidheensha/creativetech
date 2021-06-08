from django.urls import path
import newapp.views


urlpatterns = [

    path('',newapp.views.sample,name="sample"),

    ]