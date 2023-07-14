import requests
from bs4 import BeautifulSoup
import time

# for Washington
#data = requests.post("https://keraies.eett.gr/getData.php", data={"municipality":"Αβδήρων"}).text 

url = requests.post("https://keraies.eett.gr/getData.php", data={"municipality":"Αθηναίων", "startPage": "25"})
soup = BeautifulSoup(url.text, 'html.parser')
sites_table = soup.find('table', class_ = 'table table-striped table-condensed table-responsive')

app_ids = []

for site in sites_table.find_all('tbody'):
    rows = site.find_all('tr')
    for row in rows:
        data = row.find_all('td')[6]
        print(data.find('a')['onclick'])
        app_ids.append(data.find('a')['onclick'])
        # time.sleep(2)



#print(data)
print(url.status_code)
print(app_ids[0])