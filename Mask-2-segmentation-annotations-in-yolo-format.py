import imutils
import cv2
import glob
import os
from pathlib import Path


for image in os.listdir('C:/Users/Adeel/Desktop/mask_images/input'):
    mask1 = cv2.imread(os.path.join('C:/Users/Adeel/Desktop/mask_images/input', image))
    name = os.path.basename(os.path.join('C:/Users/Adeel/Desktop/mask_images/input', image))
    name = os.path.splitext(name)[0]
    print(name)
    gray = cv2.cvtColor(mask1,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # thresh = cv2.bitwise_not(thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    cv2.drawContours(mask1, [c], -1, (0, 255, 255), 2)
    cv2.circle(mask1, extLeft, 8, (0, 0, 255), -1)
    cv2.circle(mask1, extRight, 8, (0, 255, 0), -1)
    cv2.circle(mask1, extTop, 8, (255, 0, 0), -1)
    cv2.circle(mask1, extBot, 8, (255, 255, 0), -1)
    print(extLeft)
    print(extRight)
    print(extTop)
    print(extBot)
    # cv2.imshow("mask1", mask1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() 
    
    save_dir = str("C:/Users/Adeel/Desktop/mask_images/output")
    
    # p = Path('D:/SKU/6-PDF/Docs-Dataset/txts/')
    

    
    txt_path = str(save_dir)
    # # txt_path = str(save_dir / 'labels' / p.stem)
    
    x1, y1 = extLeft
    x2,y2 = extTop
    x3,y3 = extRight
    x4,y4 = extBot
    
    
    cls=0
    
    line = cls, x1, y1,x2,y2,x3,y3,x4,y4
    
    # for i, det in enumerate(c):  # per image
    #         c += 1

    name = os.path.join('C:/Users/Adeel/Desktop/mask_images/output',name)
    print(name)
    with open(f'{name}.txt', 'a') as f:
        f.write(('%s ' * len(line)).rstrip() % line + '\n')
        
    
