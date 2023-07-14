import requests
from bs4 import BeautifulSoup

app_ids = [101743, 102255, 102405, 87572, 59721, 27233, 28723, 22310, 44633, 100049, 100866, 102513, 102616, 100357, 40796, 46330, 42538, 43981, 59711, 30246, 30252, 30248, 100354, 100926, 100526]

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

# url = requests.post("https://keraies.eett.gr/getDetails.php", data={"appId":"140829"})
