"""
    Name : Aseem Thapa
    ID : 1001543178
"""

import numpy as np
import matplotlib.pyplot as mp
from matplotlib.image import imread
from skimage.feature import match_template

def RGB_to_BW(img):
    #Apply luma transform to convert RGB image to BW images
    return np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])

def showImages(img1BW,img2BW):
    """SHOW THE IMAGES:"""
    output = mp.figure(figsize=(12, 12))
    output.add_subplot(2,1,1)
    mp.imshow(img1BW, cmap = 'gray')
    mp.title('Image in which to find')
    output.add_subplot(2,1,2)
    mp.imshow(img2BW, cmap = 'gray')
    mp.title('Image that is to be found') 
    mp.tight_layout()
    mp.show() 
    
def findImage(mainImage, template) :
    #READ THE IMAGES:
    img1 = imread('ERBwideColorSmall.jpg') #Image in which template is to be found 
    img2 = imread('ERBwideTemplate.jpg') #Image containing Template
    
    """CONVERTING IMAGES TO BLACK AND WHITE"""
    img1BW = RGB_to_BW(img1) 
    img2BW = RGB_to_BW(img2)
    """DONE"""   
    
    showImages(img1BW,img2BW)
    
    """FIND THE NORMALIZED CROSS CORRELATION"""
    result = match_template(img1BW,img2BW)

    r, c = np.where(result == np.max(result))
    
    r = int(r)
    c = int(c)
    """BLACK OUT THE REMOVED PART"""
    for i in range(0,len(img2BW)): #ROW
        for j in range (0,len(img2BW[0])): #COLUMN
            img1BW[i+r][j+c] = 0   
   
    mp.imshow(img1BW)  
         
    return r, c

   
    
#############  main  #############
# this function should be how your code knows the names of
#   the images to process
# it will return the coordinates of where the template best fits

if __name__ == "__main__":
    mainImage = "ERBwideColorSmall.jpg"
    template = "ERBwideTemplate.jpg"
    #findImage(mainImage, template)
    r, c = findImage(mainImage, template)

    print("coordinates of match = (%d, %d)" % (r, c))
