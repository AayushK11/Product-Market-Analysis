import numpy as np
import tkinter as tk
import pandas as pd
from tkinter.filedialog import askopenfilename

#Module takes 1 parameter - csvFile path
#Module returns 2 lists - trainData and testData
#Each list has a tuple as an element
#Each tuple contains (Image, Emotion id)
#Each image is 48x48 in size

def getFile():
    root = tk.Tk()
    root.withdraw()
    return askopenfilename()

def convertImage(pixels_1d):
    pixels_2d = np.reshape(pixels_1d,(48,48))
    pixels_2d = np.array(pixels_2d,dtype=np.uint8)
    return pixels_2d

def splitTrainTest(filepath):
    trainData = []
    testData = []
    csvFile = pd.read_csv(filepath)
    for i in csvFile.index:
        usage = csvFile.iloc[i][2]
        if(usage == "Training"):
            pixels_1d = csvFile.iloc[i][1].split(' ')
            pixels_2d = convertImage(pixels_1d)
            emotion = csvFile.iloc[i][0]
            currentSet = (pixels_2d, emotion)
            trainData.append(currentSet)
        else:
            pixels_1d = csvFile.iloc[i][1].split(' ')
            pixels_2d = convertImage(pixels_1d)
            emotion = csvFile.iloc[i][0]
            currentSet = (pixels_2d, emotion)
            testData.append(currentSet)
    return trainData, testData

def getFilePath():
    filepath = getFile()
    trainData, testData = splitTrainTest(filepath)
    return trainData, testData