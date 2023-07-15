import pandas as pd
from helium import *
from bs4 import BeautifulSoup

url = "https://www.speedtest.net/performance/greece"

browser = start_chrome(url, headless=True)

soup = BeautifulSoup(browser.page_source, "html.parser")

urls = []

for li in soup.find_all(class_="performance-place-listing-group"):
    print('https://www.speedtest.net' + li.a.get('href'))
    urls.append('https://www.speedtest.net' + li.a.get('href'))

for li in soup.find_all('li'):
    if '/performance/greece/' in li.a.get('href'):
        print('https://www.speedtest.net' + li.a.get('href'))
        urls.append('https://www.speedtest.net' + li.a.get('href'))

print(urls[:5])