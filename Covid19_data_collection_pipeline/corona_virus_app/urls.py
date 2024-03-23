
from django.urls import path
from . import views

urlpatterns = [
    
    #Admin user actions
    path('pie/',views.piePlotOfEachStatic,name="pie"),
]