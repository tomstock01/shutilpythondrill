# Python version 2.7.12
# Author: Tom Stock
# Shutil drill

import shutil
import os


toFolder = 'C:/Users/thoma/Desktop/FolderB'
fromFolder = 'C:\\Users\\thoma\\Desktop\\FolderA\\'

def filetransfer(src, dst):
    array1 = os.listdir(src)
    for i in array1:
        transfiles = src + i
        shutil.move(transfiles,dst)
        print transfiles

filetransfer(fromFolder, toFolder)
