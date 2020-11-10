import numpy as np
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.utils.np_utils import to_categorical as tcg
from keras.layers.convolutional import MaxPooling2D, Convolution2D
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from get_data import *

#10 layer ConvNet to analyse expressions
#Layer 1,2 -> 16 filters. 7,7 kernel size. Relu activation. 30% Dropout
#Layer 3,4 -> 32 filters. 5,5 kernel size. Relu activation. 2,2 MaxPooled. 30% Dropout
#Layer 5,6 -> 64 filters. 3,3 kernel size. Relu activation. 2,2 MaxPooled. 30% Dropout
#Layer 7,8 -> 16 filters. 7,7 kernel size. Relu activation. 30% Dropout
#Layer 9 -> Flattened connected with 256 nodes. Relu activated. 50% Dropout
#Layer 10 -> Connected with 7 nodes. Softmax activated.

#Accuracy -> 60.83% Train. 55.77% Test
#Saced as CNN_model.json with weights as CNN_weights.h5

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
    xtr = xtr.reshape(xtr.shape[0], xtr.shape[1], xtr.shape[2] ,1).astype('float32')/32
    xte = xte.reshape(xte.shape[0], xte.shape[1], xte.shape[2], 1).astype('float32')/32
    ytr = tcg(ytr)
    yte = tcg(yte)
    return xtr, ytr, xte, yte

def model_structure(xtr, ytr, xte, yte):
    model = Sequential()

    model.add(Convolution2D(filters=16, kernel_size=(7, 7))) #48-46
    model.add(Convolution2D(filters=16, kernel_size=(7, 7))) #46-44
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    model.add(Convolution2D(filters=32, kernel_size=(5, 5))) #44->42
    model.add(Convolution2D(filters=32, kernel_size=(5, 5))) #42->40
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))                #40->20
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    model.add(Convolution2D(filters=64, kernel_size=(3, 3))) #20->18
    model.add(Convolution2D(filters=64, kernel_size=(3, 3))) #18->16
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))                #16->8
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    model.add(Convolution2D(filters=128, kernel_size=(3, 3))) #8->6
    model.add(Convolution2D(filters=128, kernel_size=(3, 3))) #6->4
    model.add(Activation('relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation="softmax"))

    model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=['accuracy'])
    callback_function = [EarlyStopping(patience=5, restore_best_weights=True)]
    history = model.fit(x=xtr, y=ytr, validation_data=(xte, yte), epochs=200, batch_size=256, callbacks=callback_function)

    print("<-------------------Model Trained. Saving as JSON File------------------->")

    model_json = model.to_json()
    with open("Model\CNN_model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("Model\CNN_weights.h5")
    plot_graph(history)

def plot_graph(history):
    plt.plot(history.history["accuracy"])
    plt.plot(history.history["val_accuracy"])
    plt.legend(["Train", "Test"], loc="upper left")
    plt.title("Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.show()

    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])
    plt.legend(["Train", "Test"], loc="upper left")
    plt.title("Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.show()

def load_model():
    json_file = open("Model\CNN_model.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("Model\CNN_weights.h5")
    return loaded_model

def create_cnn_model():
    train_data, test_data = get_file_path()
    xtr, ytr, xte, yte = split_data(train_data, test_data)
    print("<-------------------Training Model------------------->")
    model_structure(xtr, ytr, xte, yte)