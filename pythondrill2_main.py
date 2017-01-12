# Python version 2.7.12
# Author: Tom Stock
# Shutil drill

import shutil


array1 = ['C:/Users/thoma/Desktop/FolderA/doc1.txt','C:/Users/thoma/Desktop/FolderA/doc2.txt',
          'C:/Users/thoma/Desktop/FolderA/doc3.txt','C:/Users/thoma/Desktop/FolderA/doc4.txt']

for i in range(len(array1)):
    shutil.move(array1[i],'C:/Users/thoma/Desktop/FolderB')
    print array1[i]

