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


from .models import Covid19LastCases

from .cron import scrape_data_and_insert_to_db

#Variable that can be everytime overrite to register the connected users actions
user_actions_logger = logging.getLogger('user_actions')


def piePlotOfEachStatic(request):
    # user_actions_logger.info(f"L'administrateur {request.user.first_name} {request.user.last_name} a consulté la page d'accueil des admins.")
    
    if request.method=="POST":
        country = request.POST.get('country',"")
        date_saved = request.POST.get('date_saved',"")
        
        if country and date_saved:
            filtered_records = Covid19LastCases.objects.filter(
                Q(country__icontains=country) & Q(date_saved=date_saved)
            ).first()
        elif country:
            filtered_records = Covid19LastCases.objects.filter(country__icontains=country).first()
        elif date_saved:
            filtered_records = Covid19LastCases.objects.filter(date_saved=date_saved).first()
        else:
            # If neither country nor date_saved is provided, return None
            filtered_records = None
        
        if filtered_records is not None:
            print(filtered_records.id)
            # user_actions_logger.info(f"Utilisateur {request.user.first_name} {request.user.last_name} a créé une entreprise de nom : {entrep.nom}.")
            context={
        
            "instance":filtered_records
        
                  }
            return render(request,"corona_virus_app/pie_views.html",context)
        
        return redirect("home")
    
    return redirect("home")
    
    
    context={
        
        
        
        }
    return render(request,"corona_virus_app/pie_views.html",context)


# Add news statistics for some countries

def registerNewStatistics(request):
    
    # user_actions_logger.info(f"L'administrateur {request.user.first_name} {request.user.last_name} a consulté la page d'accueil des admins.")
    context={
        
        
        
        }
    return render(request,"corona_virus_app/register_static.html",context)

    
def uploadLastNewsCasesFromTheWebsite(request):
    
  
    
    
    
    # user_actions_logger.info(f"L'administrateur {request.user.first_name} {request.user.last_name} a consulté la page d'accueil des admins.")
    context={
        
        
        
        }
    return render(request,"corona_virus_app/upload_last.html",context)


def all_statics(request):
    
    all_cases = Covid19LastCases.objects.all()
    
    last_20 = Covid19LastCases.objects.order_by('-date_saved')[:20]
    
    countries = [
        'USA', 'India',
        'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Australia',
        'Vietnam', 'Taiwan', 'Argentina', 'Netherlands', 'Mexico', 'Iran', 'Indonesia', 'Poland', 'Colombia',
        'Greece', 'Austria', 'Portugal', 'Ukraine', 'Chile', 'Malaysia', 'Canada', 'Belgium', 'Israel', 'DPRK',
        'Thailand', 'Czechia', 'Peru', 'Switzerland', 'Philippines', 'South Africa', 'Romania', 'Denmark',
        'Singapore', 'Hong Kong', 'Sweden', 'Serbia', 'New Zealand', 'Iraq', 'Hungary', 'Bangladesh', 'Slovakia',
        'Georgia', 'Jordan', 'Ireland', 'Pakistan', 'Finland', 'Norway', 'Kazakhstan', 'Lithuania', 'Slovenia',
        'Bulgaria', 'Croatia', 'Guatemala', 'Morocco', 'Lebanon', 'Costa Rica', 'Bolivia', 'Tunisia', 'Cuba',
        'Ecuador', 'UAE', 'Panama', 'Uruguay', 'Mongolia', 'Nepal', 'Belarus', 'Latvia', 'Saudi Arabia', 'Paraguay',
        'Azerbaijan', 'Bahrain', 'Cyprus', 'Dominican Republic', 'Sri Lanka', 'Kuwait', 'Myanmar', 'Moldova',
        'Estonia', 'Palestine', 'Venezuela', 'Egypt', 'Qatar', 'Libya', 'Ethiopia', 'Réunion', 'Honduras', 'Armenia',
        'Bosnia and Herzegovina', 'Oman', 'Luxembourg', 'North Macedonia', 'Zambia', 'Kenya', 'Brunei', 'Albania',
        'Botswana', 'Montenegro', 'Algeria', 'Nigeria', 'Zimbabwe', 'Uzbekistan', 'Mozambique', 'Afghanistan',
        'Martinique', 'Laos', 'Iceland', 'Kyrgyzstan', 'Guadeloupe', 'El Salvador', 'Trinidad and Tobago', 'Maldives',
        'Namibia', 'Uganda', 'Ghana', 'Jamaica', 'Cambodia', 'Rwanda', 'Cameroon', 'Malta', 'Barbados', 'Angola',
        'Channel Islands', 'DRC', 'French Guiana', 'Malawi', 'Senegal', 'Ivory Coast', 'Suriname', 'New Caledonia',
        'French Polynesia', 'Eswatini', 'Guyana', 'Belize', 'Fiji', 'Madagascar', 'Cabo Verde', 'Sudan', 'Mauritania',
        'Bhutan', 'Syria', 'Burundi', 'Seychelles', 'Gabon', 'Andorra', 'Papua New Guinea', 'Curaçao', 'Aruba',
        'Tanzania', 'Mauritius', 'Mayotte', 'Togo', 'Guinea', 'Bahamas', 'Isle of Man', 'Lesotho', 'Haiti',
        'Faeroe Islands', 'Mali', 'Cayman Islands', 'Saint Lucia', 'Benin', 'Somalia', 'Micronesia', 'Macao',
        'San Marino', 'Solomon Islands', 'Congo', 'Timor-Leste', 'Burkina Faso', 'Liechtenstein', 'Gibraltar',
        'Grenada', 'Bermuda', 'South Sudan', 'Nicaragua', 'Tajikistan', 'Equatorial Guinea', 'Monaco', 'Samoa',
        'Tonga', 'Marshall Islands', 'Dominica', 'Djibouti', 'CAR', 'Gambia', 'Saint Martin', 'Vanuatu', 'Greenland',
        'Yemen', 'Caribbean Netherlands', 'Sint Maarten', 'Eritrea', 'Niger', 'St. Vincent Grenadines', 'Guinea-Bissau',
        'Comoros', 'Antigua and Barbuda', 'Liberia', 'Sierra Leone', 'Chad', 'British Virgin Islands', 'Cook Islands',
        'Sao Tome and Principe', 'Turks and Caicos', 'Saint Kitts and Nevis', 'Palau', 'St. Barth', 'Nauru', 'Kiribati',
        'Anguilla', 'Wallis and Futuna', 'Saint Pierre Miquelon', 'Tuvalu', 'Saint Helena', 'Falkland Islands', 'Montserrat',
        'Niue', 'Diamond Princess', 'Tokelau', 'Vatican City', 'Western Sahara', 'MS Zaandam', 'China'
    ]
    
    
    
    
    context = {
        "all_cases": all_cases,
        "last_20": last_20,
        "countries": countries
    }
    
    return render(request,"corona_virus_app/all_statics.html",context)


def uploadFunction(request):
    
    scrape_data_and_insert_to_db()
    user_actions_logger.info(f"New data scraped now from the website and upload to the database!")
    
    
    return redirect('home')
    
    
    
def page404(request,exception):
    
  
    user_actions_logger.info(f"Someone access 404 page now.")
    
   
    return render(request,"corona_virus_app/404_error.html")
