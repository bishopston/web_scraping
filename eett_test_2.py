import requests
from bs4 import BeautifulSoup

# for Washington
#data = requests.post("https://keraies.eett.gr/getData.php", data={"municipality":"Αβδήρων"}).text 

url = requests.post("https://keraies.eett.gr/getDetails.php", data={"appId":"140829"})
soup = BeautifulSoup(url.text, 'html.parser')

#print(soup)
address = soup.find_all('p', class_ = 'list-group-item-heading2')

print(url.status_code)
print(address)