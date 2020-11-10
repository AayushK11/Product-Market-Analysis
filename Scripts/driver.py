from numpy.core.defchararray import mod
from model_generation import *

def create_model():
    create_cnn_model()
    read_model()

def read_model():
    model = load_model()
    print(model.summary())

if __name__ == "__main__":
    try:
        with open('CNN_model.json', 'r'):
            print("<-------------------Model Found------------------->")
            read_model()
    except FileNotFoundError:
        print("<-------------------Model does not exist. Creating one------------------->")
        create_model()