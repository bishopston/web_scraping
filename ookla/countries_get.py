import pandas as pd
from helium import *
from bs4 import BeautifulSoup

url = "https://www.speedtest.net/performance"

browser = start_chrome(url, headless=True)

soup = BeautifulSoup(browser.page_source, "html.parser")

countries = []

for li in soup.find_all('li'):
    if '/performance/' in li.a.get('href'):
        print('https://www.speedtest.net' + li.a.get('href'))
        countries.append('https://www.speedtest.net' + li.a.get('href'))

browser.quit()

print(countries[:5])
print(len(countries))