from datetime import datetime
import pandas as pd
from helium import *

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

urls = [
    "https://www.speedtest.net/performance/greece/attica/acharnes",
    "https://www.speedtest.net/performance/greece/attica/agia-paraskevi",
    "https://www.speedtest.net/performance/greece/attica/agia-varvara",
    "https://www.speedtest.net/performance/greece/attica/agioi-anargyroi",
    "https://www.speedtest.net/performance/greece/attica/agios-dimitrios",
    "https://www.speedtest.net/performance/greece/attica/agios-ioannis-rentis",
    "https://www.speedtest.net/performance/greece/attica/alimos",
    "https://www.speedtest.net/performance/greece/attica/anixi",
    "https://www.speedtest.net/performance/greece/attica/ano-liosia",
    "https://www.speedtest.net/performance/greece/attica/argyroupoli",
    "https://www.speedtest.net/performance/greece/attica/artemida",
    "https://www.speedtest.net/performance/greece/attica/athens",
    "https://www.speedtest.net/performance/greece/attica/chaidari",
    "https://www.speedtest.net/performance/greece/attica/chalandri",
    "https://www.speedtest.net/performance/greece/attica/cholargos",
    "https://www.speedtest.net/performance/greece/attica/dafni",
    "https://www.speedtest.net/performance/greece/attica/drapetsona",
    "https://www.speedtest.net/performance/greece/attica/egaleo",
    "https://www.speedtest.net/performance/greece/attica/nea-smyrni",
]

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

            if "download" in thrputs_list[i][1]:
                thrputs_list[i][1] = float(thrputs_list[i][1])
                thrputs_list_.append(thrputs_list[i][1])
            else:
                thrputs_list_.append(thrputs_list[i][1])
            # print(type(thrputs_list[i][1]))
        print(thrputs_list_)

        thrputs_per_opco["area"].append(geoarea[-1])
        thrputs_per_opco["service"].append(thrputs_list_[0])
        thrputs_per_opco["provider_name"].append(thrputs_list_[1])
        thrputs_per_opco["provider_id"].append(int(thrputs_list_[2]))
        # _date = datetime.strptime(thrputs_list_[3], "%Y-%m-%d")
        # thrputs_per_opco["period"].append(_date.strftime("%Y-%m-%d"))
        # thrputs_per_opco["period"].append(datetime.strptime(thrputs_list_[3], "%Y-%m-%d"))
        thrputs_per_opco["period"].append(thrputs_list_[3])
        thrputs_per_opco["p25_download_mbps"].append(float(thrputs_list_[4]))
        thrputs_per_opco["p75_download_mbps"].append(float(thrputs_list_[5]))

        thrputs_per_opco["area"].append(geoarea[-1])
        thrputs_per_opco["service"].append(thrputs_list_[6])
        thrputs_per_opco["provider_name"].append(thrputs_list_[7])
        thrputs_per_opco["provider_id"].append(int(thrputs_list_[8]))
        thrputs_per_opco["period"].append(thrputs_list_[9])
        thrputs_per_opco["p25_download_mbps"].append(float(thrputs_list_[10]))
        thrputs_per_opco["p75_download_mbps"].append(float(thrputs_list_[11]))

        thrputs_per_opco["area"].append(geoarea[-1])
        thrputs_per_opco["service"].append(thrputs_list_[12])
        thrputs_per_opco["provider_name"].append(thrputs_list_[13])
        thrputs_per_opco["provider_id"].append(int(thrputs_list_[14]))
        thrputs_per_opco["period"].append(thrputs_list_[15])
        thrputs_per_opco["p25_download_mbps"].append(float(thrputs_list_[16]))
        thrputs_per_opco["p75_download_mbps"].append(float(thrputs_list_[17]))


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
    "/home/alexandros/Python/web_scraping/ookla/mobile_speeds_1.csv",
    index=None,
    sep="|",
    header=False,
)
print(df.head())
