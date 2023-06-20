# import csv
import cv2
import xlrd
import urllib.parse
import urllib.request
wb = xlrd.open_workbook('Nestle Products for IR.xlsx')
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
a = 1
i = 0#62871
cnt = 2000#60354
# ---------------To test excel file---------
# class_name = sheet.cell_value(i, 3)
# class_name = str(class_name)+str(i)+".jpg"
# print(class_name)
# link = sheet.cell_value(i, 4)
# # link =  "'"+str(link)+"'"
# print(link)
# ------------------------------------------

# for i in range(sheet.nrows):
#     if a==1:
#         a=2
#         continue
#     class_name = sheet.cell_value(i, 2)
#     class_name = str(class_name)+str(i)+".jpg"
#     link = sheet.cell_value(i, 3)
#     # link =  "'"+str(link)+"'"
#     print(link)
#     print(class_name)
#     urllib.request.urlretrieve(link, class_name)
while(i<=sheet.nrows):
	try:
		class_name = sheet.cell_value(i, 2)
		class_name = str(class_name)
		print("cell No",i)

		if (class_name != 'NESCAFE SALTED CARMEL PET'):
			i = i+1
			continue
		class_name = str('coffee')+str(cnt)+".jpg"
		
		link = sheet.cell_value(i, 1)
		print(link)
		print(class_name)
		# print("cell No",i)
		urllib.request.urlretrieve(link, class_name)
	except:
		a=1
		print("Task completed")
	i = i+1
	cnt = cnt+1
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

# import urllib.request
#
# urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")
