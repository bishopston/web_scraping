import requests
from bs4 import BeautifulSoup
import time
import re


url = requests.post("https://keraies.eett.gr/getData.php", data={"municipality":"Αθηναίων", "startPage": str(25)})
soup = BeautifulSoup(url.text, 'html.parser')
sites_table = soup.find('table', class_ = 'table table-striped table-condensed table-responsive')

app_a_tags = []
app_ids = []

for site in sites_table.find_all('tbody'):
    rows = site.find_all('tr')
    for row in rows:
        data = row.find_all('td')[6]
        print(data.find('a')['onclick'])
        app_a_tags.append(data.find('a')['onclick'])
        # time.sleep(2)

for item in app_a_tags:
    app_ids.append(int(re.findall(r'\d+', item)[1]))

#print(data)
print(url.status_code)
print(app_a_tags[0])
print(app_ids)