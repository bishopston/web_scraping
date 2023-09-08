from datetime import datetime
import pandas as pd
from helium import *

from urls_get_2 import urls

df = pd.DataFrame(
    columns=[
        "country",
        "area",
        "period",
        "mobile_median_download_mbps",
        "mobile_median_upload_mbps",
        "mobile_median_latency_ms",
        "fixed_median_download_mbps",
        "fixed_median_upload_mbps",
        "fixed_median_latency_ms",
    ]
)
thrputs_per_opco = {
    "country": [],
    "area": [],
    "period": [],
    "mobile_median_download_mbps": [],
    "mobile_median_upload_mbps": [],
    "mobile_median_latency_ms": [],
    "fixed_median_download_mbps": [],
    "fixed_median_upload_mbps": [],
    "fixed_median_latency_ms": [],
}

for url in urls:
    browser = start_firefox(url, headless=True)

    geoarea = url.split("/")
    print(geoarea[-1])
    print("++++++")

    html = browser.page_source

    with open("saving.txt", "w", encoding="utf-8", errors="ignore") as f:
        f.write(html)

    file_ = open("saving.txt", "r")
    lines = file_.readlines()
    cnt = 0
    for i in range(0, len(lines)):
        if lines[i].find("placeMonthlyData") != -1:
            cnt = i
            break

    thrputs = lines[i].strip("  var placeMonthlyData = ")

    thrputs = thrputs.replace(";", "")
    thrputs = thrputs.replace("[", "")
    thrputs = thrputs.replace("]", "")
    thrputs = thrputs.replace("{", "")
    thrputs = thrputs.replace("}", "")
    thrputs = thrputs.replace('"', "")
    thrputs = thrputs.strip()

    thrputs_list = thrputs.split(",")

    print(thrputs_list)
    print("++++++")

    thrputs_list_ = []

    if len(thrputs_list) > 1:
        for i in range(len(thrputs_list)):
            if ":" in thrputs_list[i]:
                thrputs_list[i] = thrputs_list[i].split(":")

                if "mbps" in thrputs_list[i][0]:
                    thrputs_list[i][1] = float(thrputs_list[i][1])
                    thrputs_list_.append(thrputs_list[i][1])
                else:
                    thrputs_list_.append(thrputs_list[i][1])

        print(thrputs_list_)
        print("++++++")

        if "mobile" in thrputs_list[1][0] and "fixed" in thrputs_list[5][0]:
            # print("found a")
            count = 0

            while count < len(thrputs_list_):
                thrputs_per_opco["country"].append(geoarea[4])
                thrputs_per_opco["area"].append(geoarea[-1])
                thrputs_per_opco["period"].append(thrputs_list_[count])
                thrputs_per_opco["mobile_median_download_mbps"].append(
                    thrputs_list_[count + 1]
                )
                thrputs_per_opco["mobile_median_upload_mbps"].append(
                    thrputs_list_[count + 2]
                )
                thrputs_per_opco["mobile_median_latency_ms"].append(
                    thrputs_list_[count + 3]
                )
                thrputs_per_opco["fixed_median_download_mbps"].append(
                    thrputs_list_[count + 4]
                )
                thrputs_per_opco["fixed_median_upload_mbps"].append(
                    thrputs_list_[count + 5]
                )
                thrputs_per_opco["fixed_median_latency_ms"].append(
                    thrputs_list_[count + 6]
                )

                count = count + 7

        elif "fixed" in thrputs_list[1][0] and "fixed" in thrputs_list[5][0]:
            # print("found b")
            count = 0

            while count < len(thrputs_list_):
                thrputs_per_opco["country"].append(geoarea[4])
                thrputs_per_opco["area"].append(geoarea[-1])
                thrputs_per_opco["period"].append(thrputs_list_[count])
                thrputs_per_opco["mobile_median_download_mbps"].append(0)
                thrputs_per_opco["mobile_median_upload_mbps"].append(0)
                thrputs_per_opco["mobile_median_latency_ms"].append(0)
                thrputs_per_opco["fixed_median_download_mbps"].append(
                    thrputs_list_[count + 1]
                )
                thrputs_per_opco["fixed_median_upload_mbps"].append(
                    thrputs_list_[count + 2]
                )
                thrputs_per_opco["fixed_median_latency_ms"].append(
                    thrputs_list_[count + 3]
                )

                count = count + 4

        else:
            # print("found c")
            count = 0

            while count < len(thrputs_list_):
                thrputs_per_opco["country"].append(geoarea[4])
                thrputs_per_opco["area"].append(geoarea[-1])
                thrputs_per_opco["period"].append(thrputs_list_[count])
                thrputs_per_opco["mobile_median_download_mbps"].append(
                    thrputs_list_[count + 1]
                )
                thrputs_per_opco["mobile_median_upload_mbps"].append(
                    thrputs_list_[count + 2]
                )
                thrputs_per_opco["mobile_median_latency_ms"].append(
                    thrputs_list_[count + 3]
                )
                thrputs_per_opco["fixed_median_download_mbps"].append(0)
                thrputs_per_opco["fixed_median_upload_mbps"].append(0)
                thrputs_per_opco["fixed_median_latency_ms"].append(0)

                count = count + 4

    browser.quit()

df = df.assign(
    country=thrputs_per_opco["country"],
    area=thrputs_per_opco["area"],
    period=thrputs_per_opco["period"],
    mobile_median_download_mbps=thrputs_per_opco["mobile_median_download_mbps"],
    mobile_median_upload_mbps=thrputs_per_opco["mobile_median_upload_mbps"],
    mobile_median_latency_ms=thrputs_per_opco["mobile_median_latency_ms"],
    fixed_median_download_mbps=thrputs_per_opco["fixed_median_download_mbps"],
    fixed_median_upload_mbps=thrputs_per_opco["fixed_median_upload_mbps"],
    fixed_median_latency_ms=thrputs_per_opco["fixed_median_latency_ms"],
)

df.to_csv(
    "/home/alexandros/Python/web_scraping/ookla/hist_results/hist_speeds_jul23_120-end.csv",
    index=None,
    sep="|",
    header=False,
)
print(df.head())
