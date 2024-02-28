import pandas as pd

df = pd.read_csv(
    "/home/alexandros/ookla_speedtests/fixed/oct23-dec23/fixed_results_concat_oct23-dec23.csv",
    sep="|",
    encoding="utf-8",
    header=None,
    names=[
        "country",
        "area",
        "service",
        "provider_name",
        "provider_id",
        "period",
        "p25_download_mbps",
        "p75_download_mbps",
        "p50_download_mbps",
        "p50_upload_mbps",
        "p50_multiserver_latency_ms",
    ],
)

region_analytical = {"region_analytical": []}

# print(df.head())

region_list = [
    list(x) for x in zip(df["country"], df["area"], df["service"], df["provider_id"])
]

# print(region_list[0])
# print(region_list[0][1])
print(len(region_list))

uniqueList = []
duplicateList = []

for i in region_list:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)

# print(f"uniqueList: {uniqueList}")
# print(f"duplicateList: {duplicateList}")

# print(len(uniqueList))
# print(len(duplicateList))

index_found = []

for j in region_list:
    if j in duplicateList:
        current_index = region_list.index(j)
        # print(current_index)
        if current_index not in index_found:
            index_found.append(current_index)
            region_analytical["region_analytical"].append(j[1] + "-region")
        else:
            region_analytical["region_analytical"].append(j[1])
    else:
        region_analytical["region_analytical"].append(j[1])

# print(region_analytical["region_analytical"])
# print(len(region_analytical["region_analytical"]))

df = df.assign(region_analytical=region_analytical["region_analytical"])

df.drop(["area"], axis=1, inplace=True)

df = df[
    [
        "country",
        "region_analytical",
        "service",
        "provider_name",
        "provider_id",
        "period",
        "p25_download_mbps",
        "p75_download_mbps",
        "p50_download_mbps",
        "p50_upload_mbps",
        "p50_multiserver_latency_ms",
    ]
]

df.to_csv(
    "/home/alexandros/ookla_speedtests/fixed/oct23-dec23/fixed_results_concat_oct23-dec23_region.csv",
    index=None,
    sep="|",
    header=False,
)
print(df.head())
