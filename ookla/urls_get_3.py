import pandas as pd
from helium import *
from bs4 import BeautifulSoup

from countries_get import countries

urls = []
countries_ = []
url_per_country = []

for item in countries:

    start_index = len(urls)

    url_split = item.split("/")
    country = url_split[-1]
    print(country)

    browser = start_chrome(item, headless=True)

    soup = BeautifulSoup(browser.page_source, "html.parser")

    for li in soup.find_all(class_="performance-place-listing-group"):
        #print('https://www.speedtest.net' + li.a.get('href'))
        urls.append('https://www.speedtest.net' + li.a.get('href'))

    for li in soup.find_all('li'):
        if ('/performance/' + country + '/') in li.a.get('href'):
            #print('https://www.speedtest.net' + li.a.get('href'))
            urls.append('https://www.speedtest.net' + li.a.get('href'))

    stop_index = len(urls)
    url_per_country.append(stop_index - start_index)
    countries_.append(country)

print(urls[:5])
print(len(urls))

df = pd.DataFrame(list(zip(countries_, url_per_country)),
               columns =['Country', 'Num of URLs'])

df.to_csv(
    "C:/Python/web_scraping_2/web_scraping/ookla/countries_urls.csv",
    index=None,
    sep="|",
    header=True,
)
print(df.head())