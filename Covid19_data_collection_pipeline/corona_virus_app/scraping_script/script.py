from bs4 import BeautifulSoup
import requests
url="https://www.worldometers.info/coronavirus/"
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
def write_data_csv_file(url):
    data=collect_data(url)
    file="covid19_crontab_job_now.csv"
    with open(file,"w",newline="\n",encoding="utf-8") as f:
        file=csv.writer(f)
        file.writerow(data[0])
        file.writerows(data[1])
        f.close()
        
        
# write_data_csv_file(url)
        
    
    