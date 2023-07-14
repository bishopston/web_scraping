import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumrequests import Chrome

#driver = webdriver.Chrome(executable_path=r'C:\selenium\\chromedriver.exe')
webdriver = Chrome(executable_path=r'C:\selenium\\chromedriver.exe')

url = "https://keraies.eett.gr"


response = webdriver.request('POST', 'https://keraies.eett.gr/getData.php', data={"municipality":"Αβδήρων"})

webdriver.get(url)
webdriver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[7]/a').click()

print(response)
