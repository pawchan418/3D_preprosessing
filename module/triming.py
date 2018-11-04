#%%
import pandas as pd

class Triming():
    def __init__(self):
        print("triming start")
    
    def triming(self, file_name, file_path, dir):
        col_names = ['{0:02d}'.format(i) for i in range(512)]
        df = pd.read_csv(file_path, encoding="shift-jis", names=col_names)
        df = df[4:]
        df.to_csv('{0}/{1}triming.csv'.format(dir, file_name), encoding="utf-8", header=None, index=False)
  