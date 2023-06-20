import os
import glob

import csv

path = os.chdir("C:/Users/Adeel/Desktop/PDF_DOCS_stufff/remove_bg/output") #Here put the path of your folder where your images are stored

image_name = "document" #Here, enter the name you want your images to have

i =0

for file in os.listdir(path):

    new_file_name =  image_name + str(i) + ".png" #here you can change the extention of your renmamed file.
    os.rename(file,new_file_name)

    i = i + 1

input("Renamed all Images!!")