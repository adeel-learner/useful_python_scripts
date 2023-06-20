from PIL import Image
import numpy as np
import os
import sys
import cv2
# from datetime import datetime


src  = 'D:/SKU/6-PDF/2/' # path to the doc images

print(os.listdir(src))
files = os.listdir(src) # Getting the files to copy



bg_imgpath = 'D:/SKU/6-PDF/bg/bg5' #path of the background image
syn_img_path = 'D:/SKU/6-PDF/synthetic-images/'

# current_datetime = datetime.now()
# str_current_datetime = str(current_datetime)
  



for image_src in enumerate(files):
	bg = Image.open(bg_imgpath+'.png') 
	bg = bg.convert("RGBA")
	print(image_src,"image_src")
	_,imgName = image_src
	doc_img = Image.open(src+str(imgName),"r")

	# Convert image to RGBA
	doc_img = doc_img.convert("RGBA")
	  
	# Convert image to RGBA
	
	  
	# Calculate width to be at the center
	width = (bg.width - doc_img.width) // 2
	  
	# Calculate height to be at the center
	height = (bg.height - doc_img.height) // 2
	  
	# Paste the doc_img at (width, height)
	newbg = bg.paste(doc_img, (width, height), doc_img)







	# bg_copy = bg.copy()
	# doc_img_copy = doc_img.copy()
	# # doc_img_copy.resize((100,100))
	# bg_copy.paste(doc_img_copy, (50, 50))
	# png_info = bg_copy.info
	# # bg_copy.save('D:/U-2-Net-master/pdf_background/'+ imgName, **png_info)
	# bg_copy.convert('RGBA')
	bg.save(syn_img_path + imgName, format="png")


	# bg.show()
	# break
	# cv2.waitKey(0)
