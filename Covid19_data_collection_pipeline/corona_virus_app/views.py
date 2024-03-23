from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

from django.contrib.auth import login,logout, authenticate 
from django.contrib.auth.decorators import login_required
import logging
import os
import glob
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse

from django.core.files import File #used to update file field

#Variable that can be everytime overrite to register the connected users actions
user_actions_logger = logging.getLogger('user_actions')


def piePlotOfEachStatic(request):
    # user_actions_logger.info(f"L'administrateur {request.user.first_name} {request.user.last_name} a consulté la page d'accueil des admins.")
    context={
        
        
        
        }
    return render(request,"corona_virus_app/pie_views.html",context)


# Add news statistics for some countries

def registerNewStatistics(request):
    
    # user_actions_logger.info(f"L'administrateur {request.user.first_name} {request.user.last_name} a consulté la page d'accueil des admins.")
    context={
        
        
        
        }
    return render(request,"corona_virus_app/register_static.html",context)
    

