import cv2
import os
from get_data import *
from model_generation import *

#Image captured from a live video source. Reshaped and used to predict

def reshape_image(image):
    requiredsize = (48, 48)
    image = cv2.resize(image, requiredsize, interpolation=cv2.INTER_AREA)
    image = image.reshape(-1, image.shape[0], image.shape[1], 1)
    image = image.astype('float32')/32
    return image

def predict(image, model):
    output = model.predict(image)
    index = np.argmax(output)
    emotion = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Suprise", "Neutral"]
    return emotion[index]

def get_face(model):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
    cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
    haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
    cv2.ocl.setUseOpenCL(False)

    live_video = cv2.VideoCapture(0)
    while True:
        _, frame = live_video.read()
        frame = cv2.flip(frame, flipCode=1)
        
        face_cascade = cv2.CascadeClassifier(haar_model)
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            face = frame[y:y+h, x:x+w]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            face = reshape_image(face)
            text = predict(face, model)
            cv2.rectangle(frame, (x+w-150, y+h), (x+w, y+h+30), (0, 255, 0), -1)
            cv2.putText(frame, text, (x+w-100, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    live_video.release()
    cv2.destroyAllWindows()