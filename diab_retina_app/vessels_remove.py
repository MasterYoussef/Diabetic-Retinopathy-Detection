import os
import sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from skimage import io
import numpy as np
import cv2
import numpy as np

def remove_vessels(image):
    print(image)
    path="/Users/hp/Desktop/detection-diabetique/diab_retina_app/test/"+ str(image)
    #img = Image.open(os.path.dirname(__file__) + '/test/' + image)
    img = cv2.imread(path)
    #path="image/05_test.jpg"
    b,g,r = cv2.split(img)
    clahe = cv2.createCLAHE(clipLimit=0.4, tileGridSize=(17,17))
    g = clahe.apply(g)
# Convert the image to 8-bit dept
    gray_8bit = cv2.convertScaleAbs(g)
    th = cv2.adaptiveThreshold(gray_8bit, 220, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21,3)
    
#remove small objects
    kernel = np.ones((1,1),np.uint8)
    opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
    
#fill gaps in vessels
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    
# Extract the vessels as a binary image
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contour_img = np.zeros_like(g)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        if (area >50 and perimeter>650):
            cv2.drawContours(contour_img, [cnt], 0, 250,4)
    vessels = cv2.bitwise_and(closing, contour_img)     
    vessels = cv2.bitwise_not(vessels)
    
    blur = cv2.GaussianBlur((vessels),(3,3),0)  
    thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY)[1]
    vessels = cv2.bitwise_not(thresh)
    new_path="/Users/hp/Desktop/detection-diabetique/diab_retina_app/test2/"+ str(image)
    print("path:", new_path)
    cv2.imwrite(new_path,thresh)