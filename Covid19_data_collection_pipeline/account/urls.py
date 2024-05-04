
from django.urls import path
from . import views

urlpatterns = [
    #AUTHENTICATION
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
    # HOME PAGE BASED ON THE TYPE OF USER
    path('home/',views.home,name="home"),
]