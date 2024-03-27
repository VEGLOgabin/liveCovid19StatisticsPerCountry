
from django.urls import path
from . import views

urlpatterns = [
    
    #Admin user actions
    path('',views.all_statics, name = "home"),
    path('pie/',views.piePlotOfEachStatic,name="pie"),
    path('upload/',views.uploadLastNewsCasesFromTheWebsite, name="UploadLastNewsCasesFromTheWebsite"),
    path('scraper/',views.uploadFunction, name="ScraperFunction")
]