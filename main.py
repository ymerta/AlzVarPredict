import pandas as pd 
df = pd.read_csv("dataset1/vv_table_download-2025224181021.txt", sep="\t",header=None)
print(df.columns)
