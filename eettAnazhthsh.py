import requests
from bs4 import BeautifulSoup
import time
import re
import math
import sys

URL = "https://keraies.eett.gr/anazhthsh.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

municipalities = soup.find_all('option', style = 'color:black;')
municipalities_stripped = []

for i in municipalities:
    municipalities_stripped.append(i.text.strip())

print(municipalities_stripped[:5])


for i in municipalities_stripped[:3]:
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
            print(app_ids)

            for id in app_ids:
                url = requests.post("https://keraies.eett.gr/getDetails.php", data={"appId":id})
                soup = BeautifulSoup(url.text, 'html.parser')

                details = soup.find_all('p', class_ = 'list-group-item-heading2')

                address = details[0].text
                location_id = details[1].text
                municipality = details[2].text
                name = details[3].text
                department = details[4].text
                latitude = details[5].text
                company = details[6].text
                longitude = details[7].text
                licensing = soup.find('span', style="color:#625F5F").text

                print(url.status_code)
                print(address)
                print(location_id)
                print(municipality)
                print(name)
                print(department)
                print(latitude)
                print(company)
                print(longitude)
                print(licensing)

