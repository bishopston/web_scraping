import requests
from bs4 import BeautifulSoup
import time
import re
import math
import sys
import pandas as pd

df = pd.DataFrame(columns=['address', 'location_id', 'municipality', 'name', 'department', 'latitude', 'company', 'longitude', 'licensing', 'category'])
base_station = {"address":[], "location_id":[], "municipality":[], "name":[], "department":[], "latitude":[], "company":[], "longitude":[], "licensing":[], "category":[]}

URL = "https://keraies.eett.gr/anazhthsh.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

municipalities = soup.find_all('option', style = 'color:black;')
municipalities_stripped = []

for i in municipalities:
    municipalities_stripped.append(i.text.strip())

print(municipalities_stripped[:5])


for i in municipalities_stripped[:2]:
    url = requests.post("https://keraies.eett.gr/getData.php", data={"municipality":i, "startPage": str(0)})
    soup = BeautifulSoup(url.text, 'html.parser')

    try:
        results = soup.find('div', class_ = 'alert my-alert2')
    except:
        print(sys.exc_info()[1])

    if results is not None:   
        results_no = int(re.findall(r'\d+', results.text)[0])
        pages = int(math.ceil(results_no / 25))

    # print(results_no)
    # print(pages)

        for j in range(pages):
            url = requests.post("https://keraies.eett.gr/getData.php", data={"municipality":i, "startPage": str(j*25)})
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

            # print(url.status_code)
            # print(app_ids)

            for id in app_ids:
                url = requests.post("https://keraies.eett.gr/getDetails.php", data={"appId":id})
                soup = BeautifulSoup(url.text, 'html.parser')

                details = soup.find_all('p', class_ = 'list-group-item-heading2')

                address = details[0].text.strip()
                location_id = details[1].text.strip()
                municipality = details[2].text.strip()
                name = details[3].text.strip()
                department = details[4].text.strip()
                latitude = details[5].text.strip()
                company = details[6].text.strip()
                longitude = details[7].text.strip()
                licensing = soup.find('span', style="color:#625F5F").text.strip()
                if 'Όχλησης' in licensing:
                    category = 'micro'
                else:
                    category = 'macro'

                try:
                    base_station["address"].append(address)
                    base_station["location_id"].append(location_id)
                    base_station["municipality"].append(municipality)
                    base_station["name"].append(name)
                    base_station["department"].append(department)
                    base_station["latitude"].append(latitude)
                    base_station["company"].append(company)
                    base_station["longitude"].append(longitude)
                    base_station["licensing"].append(licensing)
                    base_station["category"].append(category)

                    print('%s added %d' % (name, len(base_station["address"]),))

                except:
                    print('%s already exists or wrong data' % (name,))

                time.sleep(1)

df = df.assign(address = base_station["address"], location_id = base_station["location_id"], municipality = base_station["municipality"], name = base_station["name"], department = base_station["department"], latitude = base_station["latitude"], company = base_station["company"], longitude = base_station["longitude"], licensing = base_station["licensing"], category = base_station["category"])

df.to_csv("/home/alexandros/Python/web_scraping/antennas_test_ubuntu.csv", index=None, sep='|', header=False)
print(df.head())