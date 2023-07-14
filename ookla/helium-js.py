from helium import *
from bs4 import BeautifulSoup

# from chromedriver_autodownloader import download_chromedriver


# download_chromedriver()

url = "https://quotes.toscrape.com/js/"

browser = start_chrome(url, headless=True)

html = browser.page_source
print(html)
""" soup = BeautifulSoup(browser.page_source, "html.parser")

quotes = soup.find_all("div", {"class": "quote"})
for item in quotes:
    print(item.find("span", {"class": "text"}).text)
 """
# print(soup.title.text)
# print(quotes)
