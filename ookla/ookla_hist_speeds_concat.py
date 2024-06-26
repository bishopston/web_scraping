import pandas as pd
import glob
import os

path = r"/home/alexandros/ookla_speedtests/hist/jan24"  # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))

# print(all_files)

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None, sep="|")
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv(
    "/home/alexandros/ookla_speedtests/hist/jan24/hist_results_concat_jan24.csv",
    index=None,
    sep="|",
    header=False,
)
