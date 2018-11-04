#%%
import os
import glob
import pathlib
import re
from module import triming

#%%
input_file_name = glob.glob('./input/**/*.csv', recursive=True)
for i in range(len(input_file_name)):
    input_file_name[i] = input_file_name[i][-18:-4]
print(input_file_name)
#%%
input_file_path2 = pathlib.Path('./input')
input_file_path3 = list(input_file_path2.glob('**/*.csv'))

#%%
trimmeddirpath = './trim'
#%%
os.mkdir(trimmeddirpath)
#%%
trim = triming.Triming()
#%%
#%%
for fileNo in range(len(input_file_path3)):
    trim.triming(input_file_name[fileNo], input_file_path3[fileNo], trimmeddirpath)