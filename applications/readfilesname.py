import os

def getFlist(path):
    for root, dirs, files in os.walk(r"G:"):
        print('root_dir:', root)
        print('sub_dirs:', dirs)
        print('files:', files)
    return files
resDir = 'res'
flist = getFlist(resDir)