import glob
import pathlib

class ReadFileNameAndPath():
    
    def __init__(self):
        print("Reading start")

    def readfilename(self, dirname):
        file_names = glob.glob('./{0}/**/*.csv'.format(dirname), recursive=True)
        for i in range(len(file_names)):
            file_names[i] = file_names[i][-18:-4]
        return file_names

    def readfilepath(self, dirname):
        file_paths = pathlib.Path('./{0}'.format(dirname))
        file_paths2 = list(file_paths.glob('**/*.csv'))
        return file_paths2
