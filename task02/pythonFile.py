import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

image_path1 = r'D:\drive-download-20240511T193904Z-001\1.png'
image_path2 = r'D:\drive-download-20240511T193904Z-001\2.png'
image_path3 = r'D:\drive-download-20240511T193904Z-001\3.png'
image_path4 = r'D:\drive-download-20240511T193904Z-001\4.png'

# img = []
img1 = Image.open(image_path1)
img2 = Image.open(image_path2)
img3 = Image.open(image_path3)
img4 = Image.open(image_path4)

def model(img):
    height, width = img.size

    pixels = np.zeros((width, height), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            pixel = sum(img.getpixel((i, j)))
            pixels[i, j] = pixel
            
    return pixels

print(model(img3))