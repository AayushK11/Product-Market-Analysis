from tkinter import font
from model_generation import *
from model_prediction import *
import os
from tkinter import *
from PIL import ImageTk, Image

class Graphic():
    def __init__(self):
        self.root = Tk()
        self.root.title("Product Market Analysis")
        self.root.config(bg="#0E0C24")
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.root.geometry("500x500+100+100")
        self.root.frame = Frame(self.root ,bg="#0E0C24", width  =500, height=500).pack()

        logo_icon = Image.open('Images\PMA_Icon.png')
        logo_icon = logo_icon.resize((250, 250))
        logo_icon = ImageTk.PhotoImage(logo_icon)
        self.i1 = Button(self.root.frame, image=logo_icon, bg="#0E0C24", bd=0, width=250, height=250)
        self.i1.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.l1 = Label(self.root.frame, text="Product Market Analysis", fg="#0BFB2E", bg="#0E0C24", font="None 24 bold")
        self.l1.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.root.after(3000, self.login)
        self.root.mainloop()

    def login(self):
        self.root.quit()
        self.l1.destroy()
        self.i1.destroy()
        self.root.title("Product Market Analysis - Login")
        self.root.mainloop()


def create_model():
    create_cnn_model()
    start_emotion_prediction()

def start_emotion_prediction():
    model = load_model()
    average_emotion = get_face(model)
    print(average_emotion)


if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
    # try:
    #     with open('Model/CNN_Model.json', 'r'):
    #         print("<-------------------Model Found------------------->")
    #         start_emotion_prediction()
    # except FileNotFoundError:
    #     print("<-------------------Model does not exist. Creating one------------------->")
    #     create_model()
    g = Graphic()