import os
import sys
from PIL import Image
from skimage import io
import numpy as np
import cv2
import numpy as np    
    
def draw_vessels(image):   
    path="/Users/hp/Desktop/detection-diabetique/diab_retina_app/test/"+ str(image)
    path2="/Users/hp/Desktop/detection-diabetique/diab_retina_app/test2/"+ str(image)
    Original_Im = Image.open(path)
    Vessels_Im = Image.open(path2)
    Orig_pixels = Original_Im.load()
    Vessels_pixels = Vessels_Im.load()
    # loop through all pixels of the vessels Black and white image
    for y in range(Vessels_Im.size[0]):
        for x in range(Vessels_Im.size[1]):
            #print(Orig_pixels[y,x])
            if (Vessels_pixels[y,x]<1): # if pixel color between grey and white (0x80,0x80,0x80,255) --> (FF,FF,FF,255)                           
                Orig_pixels[y,x] = (255,255,255) ## Replace with the pixel in the line before         
    new_path="/Users/hp/Desktop/detection-diabetique/diab_retina_app/test3/"+ str(image)
    print("path:",new_path)
    Original_Im.save(new_path)