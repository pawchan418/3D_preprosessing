#%%
import os
import glob
import pandas as pd

dirpath = './delete'
os.mkdir(dirpath)

file_list = glob.glob('*.csv')

for file_name in file_list:
    col_names = ['{0:02d}'.format(i) for i in range(512)]
    df = pd.read_csv(file_name, encoding="shift-jis", names=col_names)
    df2 = df[4:]
    df2.to_csv('./delete/{0}delete.csv'.format(file_name), encoding="utf-8", header=None, index=False)
    