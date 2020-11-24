import numpy as np
import os
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.utils.np_utils import to_categorical as tcg
from keras.layers.convolutional import MaxPooling2D, Convolution2D
import matplotlib.pyplot as plt
from get_data import *

#Accuracy -> 68.61% Train. 65.92% Test
#Saved as CNN_model.json with weights as CNN_weights.h5
#Model Structure defined in CNN_Model_Details
#Model Loss graph is CNN_Loss_graph

def split_data(train_data, test_data):
    xtr = []
    xte = []
    ytr = []
    yte = []
    for i, j in train_data:
        xtr.append(i)
        ytr.append(j)
    for i, j in test_data:
        xte.append(i)
        yte.append(j)
    xtr = np.array(xtr)
    xte = np.array(xte)
    ytr = np.array(ytr)
    yte = np.array(yte)
    xtr = xtr.reshape(xtr.shape[0], xtr.shape[1], xtr.shape[2], 1).astype('float32')/32
    xte = xte.reshape(xte.shape[0], xte.shape[1], xte.shape[2], 1).astype('float32')/32
    ytr = tcg(ytr)
    yte = tcg(yte)
    return xtr, ytr, xte, yte

def model_structure(xtr, ytr, xte, yte):
    model = Sequential()

    model.add(Convolution2D(filters=16, kernel_size=(3, 3), padding="SAME")) 
    model.add(Convolution2D(filters=16, kernel_size=(3, 3), padding="SAME")) 
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))                                
    model.add(Dropout(0.35))

    model.add(Convolution2D(filters=32, kernel_size=(3, 3), padding="SAME")) 
    model.add(Convolution2D(filters=32, kernel_size=(3, 3), padding="SAME")) 
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))                                
    model.add(Dropout(0.35))

    model.add(Convolution2D(filters=64, kernel_size=(3, 3), padding="SAME")) 
    model.add(Convolution2D(filters=64, kernel_size=(3, 3), padding="SAME")) 
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))                                
    model.add(Dropout(0.35))

    model.add(Convolution2D(filters=128, kernel_size=(3, 3)))                
    model.add(Convolution2D(filters=128, kernel_size=(3, 3)))                
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation="softmax"))

    model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=['accuracy'])
    history = model.fit(x=xtr, y=ytr, validation_data=(xte, yte), epochs=200, batch_size=256)

    print("<-------------------Model Trained. Saving as JSON File------------------->")

    model_json = model.to_json()
    with open(resource_path("Model/CNN_Model.json"), "w") as json_file:
        json_file.write(model_json)
    model.save_weights(resource_path("Model/CNN_Weights.h5"))
    plot_graph(history)

def plot_graph(history):
    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])
    plt.legend(["Train", "Test"], loc="upper left")
    plt.title("Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.savefig(resource_path('Model/CNN_Loss.png'))
    plt.close()

def load_model():
    json_file = open(resource_path("Model/CNN_Model.json"), 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(resource_path("Model/CNN_Weights.h5"))
    return loaded_model

def create_cnn_model():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
    train_data, test_data = get_file_path()
    xtr, ytr, xte, yte = split_data(train_data, test_data)
    print("<-------------------Training Model------------------->")
    model_structure(xtr, ytr, xte, yte)