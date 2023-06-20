import os
import glob

os.chdir(r"E:/SOFIT/Data Labelling/cofee+powder+milk modifier data/modifier_panga")

for index, oldfile in enumerate(gl  ob.glob("*.txt"), start=1):

    newfile = str("Coffee_new") +'{}.txt'.format(index)
    os.rename (oldfile,newfile)