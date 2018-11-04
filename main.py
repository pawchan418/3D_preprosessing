#%%import module
import sys
import os
from datetime import datetime
from module import read_filename_and_path
from module import triming
from module import csv2png
print("start")

#%%get time
time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

#%%confirm paths of directry
inputdirpath = './input'
trimmeddirpath = './{0}trim'.format(time)
converteddirpath = './{0}output'.format(time)

if os.path.isdir('./input') == False:
    print("input was not found")
    sys.exit(1)

os.mkdir(trimmeddirpath)
os.mkdir(converteddirpath)

#%%trimming start
readinput = read_filename_and_path.ReadFileNameAndPath()
trim = triming.Triming()

file_names = readinput.readfilename(inputdirpath)
file_paths = readinput.readfilepath(inputdirpath)

for fileNo in range(len(file_names)):
    trim.triming(file_names[fileNo], file_paths[fileNo], trimmeddirpath)

#%%converting start
readtrimmed = read_filename_and_path.ReadFileNameAndPath()
convert = csv2png.Csv2Png()

trimmed_file_names = readtrimmed.readfilename(trimmeddirpath)
trimmed_file_paths = readtrimmed.readfilepath(trimmeddirpath)

#%%
for fileNo in range(len(trimmed_file_names)):
    convert.convert(trimmed_file_names[fileNo], trimmed_file_paths[fileNo], converteddirpath)