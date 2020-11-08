from numpy.lib.shape_base import split
import pandas as pd
import numpy as np
import cv2
import tkinter as tk
from tkinter.filedialog import askopenfilename
from pandas.core.arrays.sparse import dtype

#35887 Rows. 3 columns. 
#Col 1 Emotion
#Col 2 Pixels
#Col 3 Usage
#Total pixels of 1 image = 2304
#Each image is 48x48
# 0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral
#28709 training images
#7178 test images

def getFile():
    root = tk.Tk()
    root.withdraw()
    return askopenfilename()

def readFile(filepath):
    csvFile = pd.read_csv(filepath)
    for i in csvFile.index:        
        emotion_id = csvFile.iloc[i][0]
        pixels_1d = csvFile.iloc[i][1].split(' ')
        usage = csvFile.iloc[i][2]
        emotion = ["Angry","Disgust","Fear","Happy","Sad","Suprise","Neutral"]
        pixels_2d = np.reshape(pixels_1d,(48,48))
        pixels_2d = np.array(pixels_2d,dtype=np.uint8)
        showImage(pixels_2d)
        
def showImage(pixels):
    cv2.imshow("image",pixels)
    cv2.waitKey(0)

if __name__ == "__main__":
    filepath = getFile()
    readFile(filepath)