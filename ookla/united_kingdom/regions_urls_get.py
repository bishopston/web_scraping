import pandas as pd
from helium import *
from bs4 import BeautifulSoup

from regions_get import countries

urls = []

for item in countries:
    print(item)

    url_split = item.split("/")
    country = url_split[-1]
    print(country)

    browser = start_firefox(item, headless=True)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    # for li in soup.find_all(class_="performance-place-listing-group"):
    #     print('https://www.speedtest.net' + li.a.get('href'))
    #     urls.append('https://www.speedtest.net' + li.a.get('href'))

    for li in soup.find_all("li"):
        if ("/performance/united-kingdom/" + country + "/") in li.a.get("href"):
            print("https://www.speedtest.net" + li.a.get("href"))
            urls.append("https://www.speedtest.net" + li.a.get("href"))

    browser.quit()

print(urls[:5])
print(len(urls))
