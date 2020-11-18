from numpy.core.fromnumeric import product
from model_generation import *
from model_prediction import *
from graphical_components import *
import os
from tkinter import *   
from tkinter import messagebox 

class Graphic():
    #Graphical User Interface
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

        self.root.after(100, self.login)
        self.root.mainloop()

    def login(self):
        self.root.quit()
        self.root.title("Product Market Analysis - Login")
        for i in self.components:
            if isinstance(i, list):
                i.clear()
            else:
                i.destroy()

        self.components, logo_icon = login_page(self.root.frame)
        self.components[0].config(image=logo_icon)
        self.components[9].config(command=self.login_check)
        self.components[10].config(command=self.register)

        self.root.mainloop()

    def login_check(self):
        username = self.components[6].get()
        password = self.components[8].get()
        found, self.input_text, self.username = check_credentials(username, password)
        if found == 0:
            messagebox.showerror( "PMA", "Invalid Credentials")
            self.login()
        elif found == 1:
            messagebox.showinfo( "PMA", "Welcome Back User")
            # self.home_page_user()
        elif found == 2:
            messagebox.showinfo( "PMA", "Welcome Back Admin")
            self.home_page_admin()

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

    def home_page_admin(self):
        self.root.title("Product Market Analysis - Admin")
        for i in self.components:
            if isinstance(i, list):
                i.clear()
            else:
                i.destroy()

        products = []
        start = -1
        
        admin =  open('Dataset/Login_Admin', 'r')
        for line_num, line in enumerate(admin):
            if self.input_text==line:
                start = line_num
            if '_#_sep_#_' in line and line_num>start and start!=-1:
                break
            if '---->' in line and start!=-1 and line_num>start:
                product = str(line).replace('---->','').replace('\n','')
                products.append(product)

        self.var = IntVar()
        self.value = 0

        self.components, logo_icon = home_admin(self.root.frame, products, self.username)
        self.components[0].config(image=logo_icon)
        self.components[3].config(command=self.login)
        self.components[5].config(command=self.add_item_admin)
        for i in self.components[8]:
            i.config(variable=self.var, value=self.value, command=self.delete_item_admin)
            self.value+=1

        self.root.mainloop()  

    def add_item_admin(self):
        top=self.top=Toplevel(self.root)
        self.l=Label(top,text="Enter Item")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
        add_item(self.value, self.input_text)
        self.home_page_admin()

    def delete_item_admin(self):
        choice = self.var.get()
        delete_item(choice, self.input_text)
        self.home_page_admin()
        
def check_credentials(username, password):
    flag = 0
    input_text = username+"_#_sep_#_"+password+'\n'

    user = open('Dataset/Login_User', 'r')
    for credentials in user:
        if input_text==credentials:
            flag = 1
    user.close()

    admin =  open('Dataset/Login_Admin', 'r')
    for credentials in admin:
        if input_text==credentials:
            flag = 2
    admin.close()

    return flag, input_text, username

def create_account(username, password, choice):
    
    if choice==1:
        user = open('Dataset/Login_User', 'a')
        text = username+"_#_sep_#_"+password+'\n'
        user.write(text)
        user.close()

    if choice==2:
        admin = open('Dataset/Login_Admin', 'a')
        text = username+"_#_sep_#_"+password+'\n'
        admin.write(text)
        admin.close()

def add_item(value, input_text):
    out_file = []
    with open('Dataset/Login_Admin', 'r') as admin:
        in_file = admin.readlines()
        for line in in_file:
            out_file.append(line)
            if input_text==line:
                out_file.append("---->"+str(value)+'\n')
    admin.close()
    with open('Dataset/Login_Admin', 'w') as admin:
        admin.writelines(out_file)

def delete_item(choice, input_text):
    lines = []
    start = -1
    with open('Dataset/Login_Admin', 'r') as admin:
        for line_num, line in enumerate(admin):
            if input_text==line:
                start = line_num
    admin.close()
    with open('Dataset/Login_Admin', 'r') as admin:
        lines = admin.readlines()
    admin.close()
    if start!=-1:
        lines.remove(lines[start+1+choice])
    with open('Dataset/Login_Admin', 'w') as admin:
        admin.writelines(lines)

    
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