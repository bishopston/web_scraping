import pandas as pd
import glob
import os

path = r"/home/alexandros/ookla_speedtests/mobile"  # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))

# print(all_files)

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None, sep="|")
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv(
    "/home/alexandros/ookla_speedtests/mobile/mobile_results_concat_jun23_jul23_aug23.csv",
    index=None,
    sep="|",
    header=False,
)
