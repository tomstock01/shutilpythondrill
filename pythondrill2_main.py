# Python version 2.7.12
# Author: Tom Stock
# Shutil drill

import shutil
import os

array1 = os.listdir(r'C:\Users\thoma\Desktop\FolderA')

##for i in range(len(array1)):
##    #things = array1[i]
##    stuff = 'C:\\Users\\thoma\\Desktop\\FolderA\\' + array1[i]
##    shutil.move(stuff,'C:/Users/thoma/Desktop/FolderB')
##    print stuff

for i in array1:
    #things = array1[i]
    stuff = 'C:\\Users\\thoma\\Desktop\\FolderA\\' + i
    shutil.move(stuff,'C:/Users/thoma/Desktop/FolderB')
    print stuff
