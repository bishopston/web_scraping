import pandas as pd
from helium import *
from bs4 import BeautifulSoup

url = "https://www.speedtest.net/performance/greece"

browser = start_chrome(url, headless=True)

# url_list = find_all(S("ul > li > a"))

# urls = [item.web_element.value for item in url_list]

# print(urls)


# url_list = find_all(S("#ic_arrow_up"))

# urls = [item.web_element.text for item in url_list]

# print(urls)

# soup = BeautifulSoup(browser.page_source, "html.parser")

# for li in soup.find_all(class_="performance-place-listing-group"):
#     print('https://www.speedtest.net' + li.a.get('href'))

# for li in soup.find_all('li'):
#     if '/performance/greece/' in li.a.get('href'):
#         print('https://www.speedtest.net' + li.a.get('href'))

url_split = url.split("/")
country = url_split[-1]
print(country)