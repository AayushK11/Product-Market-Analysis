import numpy as np
import tkinter as tk
import pandas as pd
from tkinter.filedialog import askopenfilename

#Module takes 1 parameter - csv_file path
#Module returns 2 lists - train_data and test_data
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

#Flip image is an augmentation technique where we invert the image vertically and add it to the database

def flip_image(pixels_2d):
    flipped_imge = np.fliplr(pixels_2d)
    return flipped_imge

def get_file():
    root = tk.Tk()
    root.withdraw()
    return askopenfilename()

def convert_image(pixels_1d):
    pixels_2d = np.reshape(pixels_1d, (48, 48))
    pixels_2d = np.array(pixels_2d, dtype=np.uint8)
    return pixels_2d

def split_train_test(filepath):
    train_data = []
    test_data = []
    csv_file = pd.read_csv(filepath)
    for i in csv_file.index:
        usage = csv_file.iloc[i][2]
        if usage == "Training":
            pixels_1d = csv_file.iloc[i][1].split(' ')
            pixels_2d = convert_image(pixels_1d)
            emotion = csv_file.iloc[i][0]
            flipped_image = flip_image(pixels_2d)
            flipped_set = (flipped_image, emotion)
            current_set = (pixels_2d, emotion)
            train_data.append(current_set)
            train_data.append(flipped_set)
        else:
            pixels_1d = csv_file.iloc[i][1].split(' ')
            pixels_2d = convert_image(pixels_1d)
            emotion = csv_file.iloc[i][0]
            flipped_image = flip_image(pixels_2d)
            flipped_set = (flipped_image, emotion)
            current_set = (pixels_2d, emotion)
            test_data.append(current_set)
            test_data.append(flipped_set)
    return train_data, test_data

def get_file_path():
    try:
        with open('Dataset/fer2013.csv', 'r'):
            filepath = 'Dataset/fer2013.csv'
            print("<-------------------Dataset Found. Splitting And Cleaning Data------------------->")
    except FileNotFoundError:
        print("<-------------------Dataset Not Found------------------->")
        filepath = get_file()

    train_data, test_data = split_train_test(filepath)
    return train_data, test_data