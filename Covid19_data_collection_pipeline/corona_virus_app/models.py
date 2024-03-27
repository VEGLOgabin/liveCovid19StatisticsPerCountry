from django.db import models

# Create your models here.


# Covid 19
class Covid19LastCases(models.Model):
    
    country = models.CharField(max_length = 200 )
    totalCases = models.CharField(max_length = 50)
    newCases = models.CharField(max_length = 50)
    totalDeaths = models.CharField(max_length = 50)
    newDeaths = models.CharField(max_length = 50)
    totalRecovered = models.CharField(max_length = 50)
    newRecovered = models.CharField(max_length = 50)
    activeCases = models.CharField(max_length = 50)
    seriousCritical = models.CharField(max_length = 50)
    population = models.CharField(max_length = 100)
    continent = models.CharField(max_length = 90)
    date_saved = models.DateField(auto_now_add=True)
    
    

class TestJust(models.Model):
    
    name = models.CharField(max_length =255)
    description = models.TextField(max_length =255)
    