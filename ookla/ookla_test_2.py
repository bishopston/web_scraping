# import requests
from bs4 import BeautifulSoup

# import time
# import re
# import math
# import sys
import pandas as pd
from helium import *


url = "https://www.speedtest.net/performance/greece/attica/acharnes"
browser = start_chrome(url, headless=True)

html = browser.page_source

with open("saving.txt", "w") as f:
    f.write(html)

file_ = open("saving.txt", "r")
lines = file_.readlines()
cnt = 0
for i in range(0, len(lines)):
    if lines[i].find("providerMobileData") != -1:
        cnt = i
        break

# print(cnt)
thrputs = lines[i].strip("  var providerMobileData = ")

if thrputs is not None:

    thrputs = thrputs.replace(";", "")
    thrputs = thrputs.replace("[", "")
    thrputs = thrputs.replace("]", "")
    thrputs = thrputs.replace("{", "")
    thrputs = thrputs.replace("}", "")
    thrputs = thrputs.replace('"', "")
    thrputs = thrputs.strip()

    # for i in range(len(thrputs_list)):
    #     thrputs_list[i] = eval(thrputs_list[i])

    thrputs_list = thrputs.split(",")
    thrputs_list_ = []

    print(thrputs_list)
    for i in range(len(thrputs_list)):
        thrputs_list[i] = thrputs_list[i].split(":")
        # print(thrputs_list[i][1])
        # if isinstance(thrputs_list[i][1], float):
        #     thrputs_list_.append(float(thrputs_list[i][1]))
        # else:
        #     thrputs_list_.append(thrputs_list[i][1])
        if "download" in thrputs_list[i][1]:
            thrputs_list[i][1] = float(thrputs_list[i][1])
            thrputs_list_.append(thrputs_list[i][1])
        else:
            thrputs_list_.append(thrputs_list[i][1])
        # print(type(thrputs_list[i][1]))
    print(thrputs_list_)
    print(len(thrputs_list_))
    # for i in range(len(thrputs_list_)):
    #     print(type(thrputs_list_[i]))


# print(len(thrputs_list))
