import pandas as pd
from helium import *
from bs4 import BeautifulSoup

url = "https://www.speedtest.net/performance/united-states"

browser = start_firefox(url, headless=True)

soup = BeautifulSoup(browser.page_source, "html.parser")

countries = []

for li in soup.find_all('li'):
    if '/performance/' in li.a.get('href'):
        print('https://www.speedtest.net' + li.a.get('href'))
        countries.append('https://www.speedtest.net' + li.a.get('href'))

browser.quit()

print(len(countries))

for entry in countries:
    if entry.endswith("united-states"):
        countries.remove(entry)

strings = ['/de/', '/es', '/ja/', '/nl/', '/pt/', '/th/', 'zh-Hans', 'zh-Hant']

for country in countries:
    for string in strings:
        if string in country:
            countries.remove(country)

for entry in countries:
    if entry.endswith("states"):
        countries.remove(entry)

for entry in countries:
    if entry.endswith("states"):
        countries.remove(entry)

for entry in countries:
    if entry.endswith("states"):
        countries.remove(entry)

print(countries)
print(len(countries))

# df = pd.DataFrame(countries)

# df.to_csv(
#     "C:/Python/web_scraping_2/web_scraping/ookla/united_states/states_get.csv",
#     index=None,
#     sep="|",
#     header=False,
# )