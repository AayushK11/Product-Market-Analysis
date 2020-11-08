import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization
from keras.utils.np_utils import to_categorical as tcg
from keras.layers.convolutional import Conv2D, MaxPooling2D
from get_data import *

def createCNNModel():
    trainData, testData = getFilePath()