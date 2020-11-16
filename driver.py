from tkinter import font
from model_generation import *
from model_prediction import *
from graphical_components import *
import os
from tkinter import *   
from tkinter import messagebox 

class Graphic():
    def __init__(self):
        self.root = Tk()
        self.root.title("Product Market Analysis")
        self.root.config(bg="#0E0C24")
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.root.geometry("500x500+100+100")
        self.root.frame = Frame(self.root, bg="#0E0C24", width=500, height=500).pack()

        self.components, logo_icon = splash_screen(self.root.frame)
        self.components[0].config(image=logo_icon)

        self.root.after(3000, self.login)
        self.root.mainloop()

    def login(self):
        self.root.quit()
        self.root.title("Product Market Analysis - Login")
        for i in self.components:
            i.destroy()

        self.components, logo_icon = login_page(self.root.frame)
        self.components[0].config(image=logo_icon)
        self.components[9].config(command=self.login_check)
        self.components[10].config(command=self.register)

        self.root.mainloop()

    def login_check(self):
        username = self.components[6].get()
        password = self.components[8].get()
        found = check_credentials(username, password)
        if found == 0:
            messagebox.showerror( "PMA", "Invalid Credentials")
            self.login()
        elif found == 1:
            messagebox.showinfo( "PMA", "Welcome Back User")
            self.home_page_user()
        elif found == 2:
            messagebox.showinfo( "PMA", "Welcome Back Admin")
            # self.home_page_user()

    def register(self):
        self.root.quit()
        self.root.title("Product Market Analysis - Login")
        for i in self.components:
            i.destroy()

        self.var = IntVar()

        self.components, logo_icon = register_page(self.root.frame)
        self.components[0].config(image=logo_icon)
        self.components[10].config(variable=self.var, value=1)
        self.components[11].config(variable=self.var, value=2)
        self.components[12].config(command=self.register_check)
        self.components[13].config(command=self.login)

        self.root.mainloop()       

    def register_check(self):
        username = str(self.components[6].get())
        password = str(self.components[8].get())
        choice = self.var.get()
        if username is None or len(username)<4:
            messagebox.showerror( "PMA", "Invalid Username")
        elif password is None or len(password)<4:
            messagebox.showerror( "PMA", "Invalid Password")
        elif choice==0:
            messagebox.showerror( "PMA", "Invalid Designation")
        else:
            create_account(username, password, choice)
            messagebox.showinfo( "PMA", "Account Created Successfully")
            self.login()

    def home_page_user(self):
        self.root.quit()
        self.root.title("Product Market Analysis - Home Page")
        for i in self.components:
            i.destroy()
        
def check_credentials(username, password):
    flag = 0

    user = open('Dataset\Login_User', 'r')
    for credentials in user:
        cred = credentials.split("_#_sep_#_")
        if str(username)==cred[0] and str(password)==cred[1]:
            flag = 1
    user.close()

    admin =  open('Dataset\Login_Admin', 'r')
    for credentials in admin:
        cred = credentials.split("_#_sep_#_")
        if str(username)==cred[0] and str(password)==cred[1]:
            flag = 2
    admin.close()

    return flag

def create_account(username, password, choice):
    
    if choice==1:
        user = open('Dataset\Login_User', 'a')
        text = "\n"+username+"_#_sep_#_"+password
        user.write(text)
        user.close()

    if choice==2:
        admin = open('Dataset\Login_Admin', 'a')
        text = "\n"+username+"_#_sep_#_"+password
        admin.write(text)
        admin.close()

# def create_model():
#     create_cnn_model()
#     start_emotion_prediction()

# def start_emotion_prediction():
#     model = load_model()
#     average_emotion = get_face(model)
#     print(average_emotion)

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