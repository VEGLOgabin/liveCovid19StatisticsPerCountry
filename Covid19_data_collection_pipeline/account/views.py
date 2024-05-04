from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from .models import User
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


@login_required
def home(request):
    user_actions_logger.info(f"L'administrateur {request.user.first_name} {request.user.last_name} a consulté la page d'accueil des admins.")
    context={
        
        "user":request.user,
        
        }
    return render(request,"account/home.html",context)




#Deconnexion ici
@login_required
def logout(request):
    user_actions_logger.info(f"Utilisateur {request.user.first_name} {request.user.last_name} s'est déconnecté.")
    logout(request)
    return redirect(settings.LOGIN_URL)






#L'inscription des utilisateurs ici  
def signup(request):
    if request.method == 'POST':
        #user info
        photo=request.FILES.get('photo',"")
        country=request.POST.get('country',"")
        date_inscription=request.POST.get("date_inscription","")
        telephone=request.POST.get('telephone',"")
        sexe=request.POST.get('sexe',"")
        last_name=request.POST.get('last_name')
        first_name=request.POST.get('first_name')
        password=request.POST.get("password")
        email=request.POST.get('email')
        description = request.POST.get("description","")
        
        
            
      
        if not date_inscription:
            date_inscription=timezone.now()
            
        if not photo:
            photo=None
            
        if not telephone:
            telephone=None
        if not sexe:
            sexe=None
            
        #create user here
        user=User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email=email,
            sexe=sexe,
           country = country,
            date_inscription=date_inscription,
            telephone=telephone,
            
            photo=photo,
            description = description,
            password=password
            )
        
        if user is not None:
               
                login(request, user)
                user_actions_logger.info(f"Utilisateur {user.first_name} {user.last_name} s'est inscrit.")
                
                return redirect(settings.LOGIN_REDIRECT_URL) 
              
    return render(request, 'account/signup.html')




#L'enrégistrement des logs ici
@login_required
def user_actions_view(request):
    log_file_pattern = 'user_actions*.log'  # Modèle de nom de fichier pour les fichiers de journal
    log_files = glob.glob(log_file_pattern)
    log_entries = []
    user_actions_logger.info(f"Utilisateur {request.user.first_name} {request.user.last_name} a consulté les logs.")
    for log_file_path in sorted(log_files, reverse=True):  # Triez les fichiers du plus récent au plus ancien
        with open(log_file_path, 'r') as log_file:
            log_contents = log_file.read()
            log_entries.append({'file': log_file_path, 'contents': log_contents})

    return render(request, 'account/logs_history.html', {'log_entries': log_entries})


def login(request):
    message = ''
    if request.user.is_authenticated:
     
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user = authenticate(email=email, password=password)
        if user is not None:
                login(request, user)
                user_actions_logger.info(f"Utilisateur {request.user.first_name} {request.user.last_name} s'est connecté.")
                message = f'Bonjour, {user.get_full_name()}! Vous êtes connecté.'
               
                return redirect(settings.LOGIN_REDIRECT_URL) 
        
                
        else:
            user_actions_logger.warn(f"Un inconnu a éssayé d'accéder à votre site web voici ses informations de logs: son email: {request.POST.get('email')} , son mot de passe: {request.POST.get('password')}")
            message = 'Identifiants invalides.'
    return render(request, 'account/login.html', context={'message': message})