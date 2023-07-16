from datetime import datetime
import pandas as pd
from helium import *

from urls_get import urls

df = pd.DataFrame(
    columns=[
        "area",
        "service",
        "provider_name",
        "provider_id",
        "period",
        "p25_download_mbps",
        "p75_download_mbps",
    ]
)
thrputs_per_opco = {
    "area": [],
    "service": [],
    "provider_name": [],
    "provider_id": [],
    "period": [],
    "p25_download_mbps": [],
    "p75_download_mbps": [],
}

for url in urls:

    browser = start_chrome(url, headless=True)

    geoarea = url.split("/")
    print(geoarea[-1])

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

    thrputs = thrputs.replace(";", "")
    thrputs = thrputs.replace("[", "")
    thrputs = thrputs.replace("]", "")
    thrputs = thrputs.replace("{", "")
    thrputs = thrputs.replace("}", "")
    thrputs = thrputs.replace('"', "")
    thrputs = thrputs.strip()

    thrputs_list = thrputs.split(",")

    print(thrputs_list)

    thrputs_list_ = []

    if len(thrputs_list) > 1:

        for i in range(len(thrputs_list)):
            thrputs_list[i] = thrputs_list[i].split(":")

            if "download" in thrputs_list[i][0]:
                thrputs_list[i][1] = float(thrputs_list[i][1])
                thrputs_list_.append(thrputs_list[i][1])
            else:
                thrputs_list_.append(thrputs_list[i][1])
            # print(type(thrputs_list[i][1]))
        print(thrputs_list_)

        count = 0

        while count < len(thrputs_list_):

            thrputs_per_opco["area"].append(geoarea[-1])
            thrputs_per_opco["service"].append(thrputs_list_[count])
            thrputs_per_opco["provider_name"].append(thrputs_list_[count + 1])
            thrputs_per_opco["provider_id"].append(int(thrputs_list_[count + 2]))
            thrputs_per_opco["period"].append(thrputs_list_[count + 3])
            thrputs_per_opco["p25_download_mbps"].append(
                float(thrputs_list_[count + 4])
            )
            thrputs_per_opco["p75_download_mbps"].append(
                float(thrputs_list_[count + 5])
            )

            count = count + 6


# print(len(thrputs_list))
print(thrputs_per_opco)

df = df.assign(
    area=thrputs_per_opco["area"],
    service=thrputs_per_opco["service"],
    provider_name=thrputs_per_opco["provider_name"],
    provider_id=thrputs_per_opco["provider_id"],
    period=thrputs_per_opco["period"],
    p25_download_mbps=thrputs_per_opco["p25_download_mbps"],
    p75_download_mbps=thrputs_per_opco["p75_download_mbps"],
)

df.to_csv(
    "C:/Python/web_scraping_2/web_scraping/ookla/mobile_speeds_may23.csv",
    index=None,
    sep="|",
    header=False,
)
print(df.head())
