from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\selenium\\chromedriver.exe')

url = 'http://the-internet.herokuapp.com/login'

driver.get(url)

driver.find_element_by_xpath('//*[@id="username"]').send_keys('tomsmith')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('SuperSecretPassword!')
driver.find_element_by_xpath('//*[@id="login"]/button').click()

driver.quit()

# url = 'http://the-internet.herokuapp.com/dynamic_loading/2'

# driver.get(url)