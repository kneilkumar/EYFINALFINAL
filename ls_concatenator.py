stations_files = [
"stations_0-10.csv",
"stations_10-20.csv",
"stations_20-30.csv",
"stations_30-40.csv",
"stations_40-50.csv",
"stations_50-60.csv",
"stations_60-70.csv",
"stations_70-80.csv",
"stations_80-90.csv",
"stations_90-100.csv",
"stations_100-110.csv",
"stations_110-120.csv",
"stations_120-130.csv",
"stations_130-140.csv",
"stations_140-150.csv",
"stations_150-160.csv",
"stations_160-162.csv"
]
import pandas as pd
new_ls = pd.DataFrame()
for stations_file in stations_files:
    new_ls = pd.concat([new_ls, pd.read_csv(stations_file)], axis=0)

print(new_ls.shape)
new_ls.to_csv('new_ls_feats.csv')