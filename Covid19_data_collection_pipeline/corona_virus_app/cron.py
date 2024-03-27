import logging
from django.core.management.base import BaseCommand
from subprocess import run, PIPE
import os

import pandas as pd

from .models import TestJust, Covid19LastCases

import os
import csv
from django.conf import settings

user_actions_logger = logging.getLogger('user_actions')


from bs4 import BeautifulSoup
import requests

def collect_data(url):
    table=[]
    req=requests.get(url)
    if (req.status_code==200):
        soup=BeautifulSoup(req.content,"html.parser")
        # print(soup.prettify())
        h=soup.find("thead").find("tr")
        table_header=[]
        table_header=[i.text.strip() for i in h.find_all("th")]
        # print(header)
        table.append(table_header)
        table_body=[]
        body=soup.find("tbody").find_all('tr')
        for rows in body:
            row=rows.find_all('td')
            new_row=[j.text.strip() for j in row]
            table_body.append(new_row)
            
        table.append(table_body)  
        return table
        
   
# data=collect_data(url)
# print(data[0])

# print("Now the body!!")


# print(data[1])        
import csv
# def write_data_csv_file():
#     url="https://www.worldometers.info/coronavirus/"
#     data=collect_data(url)
#     file="covid19_crontab_job_now.csv"
#     with open(file,"w",newline="\n",encoding="utf-8") as f:
#         file=csv.writer(f)
#         file.writerow(data[0])
#         file.writerows(data[1])
#         f.close()

def write_data_csv_file():
    url = "https://www.worldometers.info/coronavirus/"
    data = collect_data(url)
    file_name = "covid19_crontab_job_now.csv"
    project_dir = settings.BASE_DIR
    file_path = os.path.join(project_dir, file_name)
    
    with open(file_path, "w", newline="\n", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data[0])
        csv_writer.writerows(data[1])
        user_actions_logger.info(f"Daily task for scraping data from web is now executed")
        f.close()


        
        
def scrape_data_and_insert_to_db():
    
    url = "https://www.worldometers.info/coronavirus/"
    data = collect_data(url)
    
    header = data[0]
    data_values = data[1]
    df = pd.DataFrame(columns=header, data=data_values)
    # List of columns to delete
    columns_to_delete = ['#', 'Tot\xa0Cases/1M pop', 'Deaths/1M pop', 'TotalTests',
                     'Tests/\n1M pop', '1 Caseevery X ppl', '1 Deathevery X ppl',
                     '1 Testevery X ppl', 'New Cases/1M pop', 'New Deaths/1M pop',
                     'Active Cases/1M pop']
    
    df = df.drop(columns=columns_to_delete)

    # New column names
    new_column_names = {'Country,Other': 'country',
                    'TotalCases': 'totalCases',
                    'NewCases': 'newCases',
                    'TotalDeaths': 'totalDeaths',
                    'NewDeaths': 'newDeaths',
                    'TotalRecovered': 'totalRecovered',
                    'NewRecovered': 'newRecovered',
                    'ActiveCases': 'activeCases',
                    'Serious,Critical': 'seriousCritical',
                    'Population': 'population',
                    'Continent': 'continent'}
    
    # Rename columns
    df = df.rename(columns=new_column_names)
    
    # Iterate over rows of the DataFrame
    for index, row in df.iterrows():
        # Create a new Covid19LastCases object
        covid_case = Covid19LastCases(
            country=row['country'],
            totalCases=row['totalCases'],
            newCases=row['newCases'],
            totalDeaths=row['totalDeaths'],
            newDeaths=row['newDeaths'],
            totalRecovered=row['totalRecovered'],
            newRecovered=row['newRecovered'],
            activeCases=row['activeCases'],
            seriousCritical=row['seriousCritical'],
            population=row['population'],
            continent=row['continent']
        )
        # Save the object to the database
        covid_case.save()

    
    
    
   
    


def my_scheduled_job():
  print("Crontab job executed successfully")
        
    
    