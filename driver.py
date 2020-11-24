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

        self.root.after(3000, self.login)
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
            self.home_page_user()
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
            if isinstance(i, list):
                i.clear()
            else:
                i.destroy()


        to_be_reviewed = []
        admin =  open(resource_path('Dataset/Login_Admin'), 'r')
        for line_num, line in enumerate(admin):
            if "---->" in line:
                item = str(line).split('####')
                item = item[0].replace('---->','').replace("\n","")
                to_be_reviewed.append(item)
        admin.close()
        
        start = -1
        already_reviewed = []
        user =  open(resource_path('Dataset/Login_User'), 'r')
        for line_num, line in enumerate(user):
            if self.input_text==line:
                start = line_num
            if '_#_sep_#_' in line and line_num>start and start!=-1:
                break
            if '---->' in line and start!=-1 and line_num>start:
                text = str(line).replace('---->','').replace('\n','')
                already_reviewed.append(text)
        user.close()

        self.products = [x for x in to_be_reviewed if x not in already_reviewed]

        self.var = IntVar()
        self.value = 0

        self.components, logo_icon = home_user(self.root.frame, self.products, self.username)
        self.components[0].config(image=logo_icon)
        self.components[3].config(command=self.logout)
        for i in self.components[7]:
            i.config(variable=self.var, value=self.value, command=self.review_item_user)
            self.value+=1

        self.root.mainloop()

    def home_page_admin(self):
        self.root.title("Product Market Analysis - Admin")
        for i in self.components:
            if isinstance(i, list):
                i.clear()
            else:
                i.destroy()

        products = []
        start = -1
        
        admin =  open(resource_path('Dataset/Login_Admin'), 'r')
        for line_num, line in enumerate(admin):
            if self.input_text==line:
                start = line_num
            if '_#_sep_#_' in line and line_num>start and start!=-1:
                break
            if '---->' in line and start!=-1 and line_num>start:
                text = str(line).replace('---->','').replace('\n','').replace("####","--")
                products.append(text)

        self.var = IntVar()
        self.value = 0

        self.components, logo_icon = home_admin(self.root.frame, products, self.username)
        self.components[0].config(image=logo_icon)
        self.components[3].config(command=self.logout)
        self.components[5].config(command=self.add_item_admin)
        for i in self.components[8]:
            i.config(variable=self.var, value=self.value, command=self.delete_item_admin)
            self.value+=1

        self.root.mainloop()  

    def add_item_admin(self):
        top=self.top=Toplevel(self.root)
        self.top.title("PMA")
        self.top.config(bg="#0E0C24")
        self.top.minsize(125, 125)
        self.top.maxsize(125, 125)
        self.top.geometry("125x125+100+100")
        self.l=Label(top,text="Enter Item", fg="#0BFB2E",bg="#0E0C24", font="None 10")
        self.l.pack(padx=(10, 10), pady=(10, 10))
        self.e=Entry(top)
        self.e.pack(padx=(10, 10), pady=(10, 10))
        self.b=Button(top,text='Ok',command=self.cleanup, fg="#0BFB2E", bg="#0E0C24", bd=2, font="None 10")
        self.b.pack()

    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
        add_item(self.value, self.input_text)
        self.home_page_admin()

    def delete_item_admin(self):
        MsgBox = tk.messagebox.askquestion('Logout','Are you sure you want to delete this item?',icon = 'warning')
        if MsgBox == 'yes':
            choice = self.var.get()
            delete_item(choice, self.input_text)
        self.home_page_admin()
        
    def review_item_user(self):
        choice = self.var.get()
        item = self.products[choice]
        MsgBox = tk.messagebox.askquestion('PMA','Are you sure you want to proceed with reviewing '+item, icon = 'warning')
        if MsgBox == 'yes':
            messagebox.showinfo( "PMA", "Reviewing will start now.\nPlease be honest about the product.\nThe system will capture your facial expressions to determine your experience with the product.\n\nPress 'q' to stop the reviewing")
            self.root.quit()
            average_emotion = start_emotion_prediction()
            messagebox.showinfo( "PMA", "Review Recorded")
            update_records(item, self.input_text, average_emotion)
        self.home_page_user()

    def logout(self):
        MsgBox = tk.messagebox.askquestion('Logout','Are you sure you want to logout',icon = 'warning')
        if MsgBox == 'yes':
            self.login()

def check_credentials(username, password):
    flag = 0
    input_text = username+"_#_sep_#_"+password+'\n'

    user = open(resource_path('Dataset/Login_User'), 'r')
    for credentials in user:
        if input_text==credentials:
            flag = 1
    user.close()

    admin =  open(resource_path('Dataset/Login_Admin'), 'r')
    for credentials in admin:
        if input_text==credentials:
            flag = 2
    admin.close()

    return flag, input_text, username

def create_account(username, password, choice):
    
    if choice==1:
        user = open(resource_path('Dataset/Login_User'), 'a')
        text = username+"_#_sep_#_"+password+'\n'
        user.write(text)
        user.close()

    if choice==2:
        admin = open(resource_path('Dataset/Login_Admin'), 'a')
        text = username+"_#_sep_#_"+password+'\n'
        admin.write(text)
        admin.close()

def add_item(value, input_text):
    out_file = []
    with open(resource_path('Dataset/Login_Admin'), 'r') as admin:
        in_file = admin.readlines()
        for line in in_file:
            out_file.append(line)
            if input_text==line:
                out_file.append("---->"+str(value)+'\n')
    admin.close()
    with open(resource_path('Dataset/Login_Admin'), 'w') as admin:
        admin.writelines(out_file)

def delete_item(choice, input_text):
    lines = []
    start = -1
    text = ''
    with open(resource_path('Dataset/Login_Admin'), 'r') as admin:
        for line_num, line in enumerate(admin):
            if input_text==line:
                start = line_num
    admin.close()
    with open(resource_path('Dataset/Login_Admin'), 'r') as admin:
        lines = admin.readlines()
    admin.close()
    if start!=-1:
        text = lines[start+1+choice]
        lines.remove(lines[start+1+choice])
    with open(resource_path('Dataset/Login_Admin'), 'w') as admin:
        admin.writelines(lines)
    text = str(text).split('####')
    with open(resource_path('Dataset/Login_User'), 'r') as user:
        lines = user.readlines()
    user.close()
    text[0] = text[0]+"\n"
    for i in lines:
        if str(i)==str(text[0]):
            lines.remove(i)
    with open(resource_path('Dataset/Login_User'), 'w') as user:
        user.writelines(lines)

def update_records(item, input_text, average_emotion):
    out_file = []
    with open(resource_path('Dataset/Login_User'), 'r') as user:
        in_file = user.readlines()
        for line in in_file:
            out_file.append(line)
            if input_text==line:
                out_file.append("---->"+str(item)+'\n')
    user.close()
    with open(resource_path('Dataset/Login_User'), 'w') as user:
        user.writelines(out_file)

    out_file = []
    line_value = "---->"+str(item)
    with open(resource_path('Dataset/Login_Admin'), 'r') as admin:
        in_file = admin.readlines()
        for line in in_file:
            line = line.replace("\n","")
            line_array = line.split("####")
            if str(line_value)==str(line_array[0]):
                out_file.append(line+"####"+average_emotion+'\n')
            else:
                out_file.append(line+"\n")
    admin.close()
    with open(resource_path('Dataset/Login_Admin'), 'w') as admin:
        admin.writelines(out_file)

def start_emotion_prediction():
    try:
        with open(resource_path('Model/CNN_Model.json'), 'r'):
            model = load_model()
            average_emotion = get_face(model)
            return average_emotion
    except FileNotFoundError:
        create_cnn_model()
        model = load_model()
        average_emotion = get_face(model)
        return average_emotion
    
if __name__ == "__main__":
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
    g = Graphic()