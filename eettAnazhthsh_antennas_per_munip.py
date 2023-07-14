import requests
from bs4 import BeautifulSoup
import time
import sys
import pandas as pd

df = pd.DataFrame(columns=['municipality', 'results'])
antennas_per_munip = {"municipality":[], "results":[]}

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

    try:
        antennas_per_munip["municipality"].append(i)
        if results.text != "0":
            antennas_per_munip["results"].append(results.text)
        else:
            antennas_per_munip["results"].append("0")

        print('%s added %d' % (i, len(antennas_per_munip["municipality"]),))

    except:
        antennas_per_munip["results"].append("0")
        print('%s already exists or wrong data' % (i,))

    time.sleep(1)

df = df.assign(municipality = antennas_per_munip["municipality"], results = antennas_per_munip["results"])

df.to_csv("/home/alexandros/Python/web_scraping/antennas_per_munip_050422.csv", index=None, sep='|', header=False)
print(df.head())
