import pandas as pd
import glob
import os

path = r"/home/alexandros/ookla_speedtests/mobile/oct23-dec23"  # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))

# print(all_files)

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None, sep="|")
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv(
    "/home/alexandros/ookla_speedtests/mobile/oct23-dec23/mobile_results_concat_oct23-dec23.csv",
    index=None,
    sep="|",
    header=False,
)
