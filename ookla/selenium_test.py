from datetime import datetime
import pandas as pd
from helium import *

from urls import urls

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.198").install())
# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.speedtest.net/performance/greece/attica/acharnes")

url = "https://www.speedtest.net/performance/greece/attica/acharnes"


browser = start_chrome(
    driver.get("https://www.speedtest.net/performance/greece/attica/acharnes"),
    headless=True,
)
