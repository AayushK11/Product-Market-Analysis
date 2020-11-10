from model_generation import *
from model_prediction import *
import os

def create_model():
    create_cnn_model()
    start_emotion_prediction()

def start_emotion_prediction():
    model = load_model()
    get_face(model)

if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
    try:
        with open('Model/CNN_Model.json', 'r'):
            print("<-------------------Model Found------------------->")
            start_emotion_prediction()
    except FileNotFoundError:
        print("<-------------------Model does not exist. Creating one------------------->")
        create_model()