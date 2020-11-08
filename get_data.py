import numpy as np
import tkinter as tk
import pandas as pd
from tkinter.filedialog import askopenfilename

#Module takes 1 parameter - csvFile path
#Module returns 2 lists - trainData and testData
#Each list has a tuple as an element
#Each tuple contains (Image, Emotion id)
#Each image is 48x48 in size

#35887 Rows. 3 columns. 
#Col 1 Emotion
#Col 2 Pixels
#Col 3 Usage
#Total pixels of 1 image = 2304
#Each image is 48x48
# 0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral
#28709 training images
#7178 test images

def get_file():
    root = tk.Tk()
    root.withdraw()
    return askopenfilename()

def convert_image(pixels_1d):
    pixels_2d = np.reshape(pixels_1d,(48,48))
    pixels_2d = np.array(pixels_2d,dtype=np.uint8)
    return pixels_2d

def split_train_test(filepath):
    trainData = []
    testData = []
    csvFile = pd.read_csv(filepath)
    for i in csvFile.index:
        usage = csvFile.iloc[i][2]
        if(usage == "Training"):
            pixels_1d = csvFile.iloc[i][1].split(' ')
            pixels_2d = convert_image(pixels_1d)
            emotion = csvFile.iloc[i][0]
            currentSet = (pixels_2d, emotion)
            trainData.append(currentSet)
        else:
            pixels_1d = csvFile.iloc[i][1].split(' ')
            pixels_2d = convert_image(pixels_1d)
            emotion = csvFile.iloc[i][0]
            currentSet = (pixels_2d, emotion)
            testData.append(currentSet)
    return trainData, testData

def get_file_path():
    filepath = get_file()
    trainData, testData = split_train_test(filepath)
    return trainData, testData