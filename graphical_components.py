from tkinter import *
import tkinter.ttk
from PIL import ImageTk, Image
import os

dark_blue = "#0E0C24"
light_green = "#0BFB2E"
light_dark_blue = "#46417F"
blue = "#112AE5"
grey = "#C5B5B5"
white = "#FFFFFF"
black = "#000000"


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def logo_reshape(x, y):
    logo_icon = Image.open(resource_path('Images/PMA_Icon.png'))
    logo_icon = logo_icon.resize((x, y))
    logo_icon = ImageTk.PhotoImage(logo_icon)
    return logo_icon

def splash_screen(frame):
    i1 = Button(frame, bg=dark_blue, bd=0, width=250, height=250)
    l1 = Label(frame, text="Product Market Analysis", fg=light_green, bg=dark_blue, font="None 24 bold")
    logo_icon = logo_reshape(250, 250)

    i1.place(relx=0.5, rely=0.4, anchor=CENTER)
    l1.place(relx=0.5, rely=0.6, anchor=CENTER)
    
    return (i1, l1), logo_icon

def login_page(frame):

    i1 = Button(frame, bg=dark_blue, bd=0, width=150, height=150)
    l1 = Label(frame, text="Product Market Analysis", fg=light_green, bg=dark_blue, font="None 12 bold")
    s1 = tkinter.ttk.Separator(frame, orient=VERTICAL)
    f1 = Frame(frame, bg=light_dark_blue, bd=2, width=400, height=250)
    l2 = Label(f1, text="Login", fg=light_green, bg=light_dark_blue, font="None 16 bold underline", underline=0)
    l3 = Label(f1, text="Username", fg=light_green, bg=light_dark_blue, font="None 16")
    t1 = Entry(f1, bg=white, fg=black, font="None 12", justify=LEFT, selectborderwidth=2)
    l4 = Label(f1, text="Password", fg=light_green, bg=light_dark_blue, font="None 16")
    t2 = Entry(f1, bg=white, fg=black, font="None 12", justify=LEFT, selectborderwidth=2, show="*")
    b1 = Button(f1, bg=blue, fg=white, font="None 12", bd=2, text="Login")
    b2 = Button(f1, bg=blue, fg=white, font="None 12", bd=2, text="New User?")
    logo_icon = logo_reshape(150, 150)
    
    i1.place(relx=0.25, rely=0.15, anchor=CENTER)
    l1.place(relx=0.75, rely=0.15, anchor=CENTER)
    s1.place(relx=0.5, rely=0.15, anchor=CENTER, relheight=0.2)
    f1.place(relx=0.5, rely=0.6, anchor=CENTER)
    l2.place(relx=0.05, rely=0.05, anchor=NW)
    l3.place(relx=0.2, rely=0.4, anchor=CENTER)
    t1.place(relx=0.7, rely=0.4, anchor=CENTER)
    l4.place(relx=0.2, rely=0.6, anchor=CENTER)
    t2.place(relx=0.7, rely=0.6, anchor=CENTER)
    b1.place(relx=0.35, rely=0.85, anchor=CENTER)
    b2.place(relx=0.65, rely=0.85, anchor=CENTER)

    return (i1, l1, s1, f1, l2, l3, t1, l4, t2, b1, b2), logo_icon

def register_page(frame):

    i1 = Button(frame, bg=dark_blue, bd=0, width=150, height=150)
    l1 = Label(frame, text="Product Market Analysis", fg=light_green, bg=dark_blue, font="None 12 bold")
    s1 = tkinter.ttk.Separator(frame, orient=VERTICAL)
    f1 = Frame(frame, bg=light_dark_blue, bd=2, width=400, height=300)
    l2 = Label(f1, text="Register", fg=light_green, bg=light_dark_blue, font="None 16 bold underline", underline=0)
    l3 = Label(f1, text="Username", fg=light_green, bg=light_dark_blue, font="None 16")
    t1 = Entry(f1, bg=white, fg=black, font="None 12", justify=LEFT, selectborderwidth=2)
    l4 = Label(f1, text="Password", fg=light_green, bg=light_dark_blue, font="None 16")
    t2 = Entry(f1, bg=white, fg=black, font="None 12", justify=LEFT, selectborderwidth=2, show="*")
    l5 = Label(f1, text="Are You a:", fg=light_green, bg=light_dark_blue, font="None 16")
    r1 = Radiobutton(f1, text="User", fg=black, bg=light_dark_blue, font="None 10 bold")
    r2 = Radiobutton(f1, text="Admin", fg=black, bg=light_dark_blue, font="None 10 bold")
    b1 = Button(f1, bg=blue, fg=white, font="None 12", bd=2, text="Sign Up")
    b2 = Button(f1, bg=blue, fg=white, font="None 12", bd=2, text="Back")
    logo_icon = logo_reshape(150, 150)

    i1.place(relx=0.25, rely=0.15, anchor=CENTER)
    l1.place(relx=0.75, rely=0.15, anchor=CENTER)
    s1.place(relx=0.5, rely=0.15, anchor=CENTER, relheight=0.2)
    f1.place(relx=0.5, rely=0.6, anchor=CENTER)
    l2.place(relx=0.05, rely=0.05, anchor=NW)
    l3.place(relx=0.2, rely=0.3, anchor=CENTER)
    t1.place(relx=0.7, rely=0.3, anchor=CENTER)
    l4.place(relx=0.2, rely=0.5, anchor=CENTER)
    t2.place(relx=0.7, rely=0.5, anchor=CENTER)
    l5.place(relx=0.2, rely=0.7, anchor=CENTER)
    r1.place(relx=0.53, rely=0.7, anchor=CENTER)
    r2.place(relx=0.7, rely=0.7, anchor=CENTER)
    b1.place(relx=0.35, rely=0.9, anchor=CENTER)
    b2.place(relx=0.65, rely=0.9, anchor=CENTER)

    return (i1, l1, s1, f1, l2, l3, t1, l4, t2, l5, r1, r2, b1, b2), logo_icon

def home_admin(frame, product, Username):

    i1 = Button(frame, bg=dark_blue, bd=0, width=100, height=100)
    l1 = Label(frame, text="Product\nMarket\nAnalysis", fg=light_green, bg=dark_blue, font="None 10 bold")
    s1 = tkinter.ttk.Separator(frame, orient=VERTICAL)
    b1 = Button(frame, bg=dark_blue, fg=white, font="None 10", bd=0, text=Username)
    f1 = Frame(frame, bg=light_dark_blue, bd=2, width=400, height=200)
    b2 = Button(frame, bg=blue, fg=white, font="None 10", bd=2, text="+")

    frames = []
    buttons = []
    labels = []

    for i in product:
        index = product.index(i)
        f_1 = Frame(f1, bg=white, bd=2, width=20, height=25)
        f_1.grid(row=index, column=0, pady=(5, 5), padx=(5, 5))
        l_1 = Label(f1, text=index, fg=black, bg=white, font="None 10")
        l_1.grid(row=index, column=0, pady=(5, 5))
        f_2 = Frame(f1, bg=white, bd=2, width=400, height=25)
        f_2.grid(row=index, column=1, pady=(5, 5), padx=(5, 5))
        l_2 = Label(f1, text=i, fg=black, bg=white, font="None 10")
        l_2.grid(row=index, column=1, pady=(5, 5))
        f_3 = Frame(f1, bg=white, bd=2, width=20, height=25)
        f_3.grid(row=index, column=2, pady=(5, 5), padx=(5, 5))
        rb_1 = Radiobutton(f1, text="x", fg=black, bg=white, bd=0, indicatoron=0, font="None 10")
        rb_1.grid(row=index, column=2, pady=(5, 5))
        frames.append(f_1)
        frames.append(f_2)
        frames.append(f_3)
        labels.append(l_1)
        labels.append(l_2)
        buttons.append(rb_1)
        
    if len(product) == 0:
        l_1 = Label(f1, text="No Items Available Yet...", fg=light_green, bg=light_dark_blue, font="None 14 bold underline", underline=0)
        l_1.place(relx=0.5, rely=0.5, anchor=CENTER)
        labels.append(l_1)
    
    logo_icon = logo_reshape(100, 100) 

    i1.place(relx=0.01, rely=0.15, anchor=W)
    l1.place(relx=0.25, rely=0.15, anchor=W)
    s1.place(relx=0.2, rely=0.15, anchor=W, relheight=0.15)
    b1.place(relx=0.9, rely=0.15, anchor=E)
    f1.place(relx=0.5, rely=0.6, anchor=CENTER)
    b2.place(relx=0.5, rely=0.9, anchor=CENTER)

    return (i1, l1, s1, b1, f1, b2, frames, labels, buttons), logo_icon

def home_user(frame, product, Username):

    i1 = Button(frame, bg=dark_blue, bd=0, width=100, height=100)
    l1 = Label(frame, text="Product\nMarket\nAnalysis", fg=light_green, bg=dark_blue, font="None 10 bold")
    s1 = tkinter.ttk.Separator(frame, orient=VERTICAL)
    b1 = Button(frame, bg=dark_blue, fg=white, font="None 10", bd=0, text=Username)
    f1 = Frame(frame, bg=light_dark_blue, bd=2, width=400, height=300)

    frames = []
    buttons = []
    labels = []

    for i in product:
        index = product.index(i)
        f_1 = Frame(f1, bg=white, bd=2, width=20, height=25)
        f_1.grid(row=index, column=0, pady=(5, 5), padx=(5, 5))
        l_1 = Label(f1, text=index, fg=black, bg=white, font="None 10")
        l_1.grid(row=index, column=0, pady=(5, 5))
        f_2 = Frame(f1, bg=white, bd=2, width=300, height=25)
        f_2.grid(row=index, column=1, pady=(5, 5), padx=(5, 5))
        l_2 = Label(f1, text=i, fg=black, bg=white, font="None 10")
        l_2.grid(row=index, column=1, pady=(5, 5))
        f_3 = Frame(f1, bg=white, bd=2, width=100, height=25)
        f_3.grid(row=index, column=2, pady=(5, 5), padx=(5, 5))
        rb_1 = Radiobutton(f1, text="Review", fg=black, bg=white, bd=0, indicatoron=0, font="None 10")
        rb_1.grid(row=index, column=2, pady=(5, 5))
        frames.append(f_1)
        frames.append(f_2)
        frames.append(f_3)
        labels.append(l_1)
        labels.append(l_2)
        buttons.append(rb_1)

    if len(product) == 0:
        l_1 = Label(f1, text="No Items Available Yet...", fg=light_green, bg=light_dark_blue, font="None 14 bold underline", underline=0)
        l_1.place(relx=0.5, rely=0.5, anchor=CENTER)
        labels.append(l_1)
        
    
    logo_icon = logo_reshape(100, 100) 

    i1.place(relx=0.01, rely=0.15, anchor=W)
    l1.place(relx=0.25, rely=0.15, anchor=W)
    s1.place(relx=0.2, rely=0.15, anchor=W, relheight=0.15)
    b1.place(relx=0.9, rely=0.15, anchor=E)
    f1.place(relx=0.5, rely=0.6, anchor=CENTER)

    return (i1, l1, s1, b1, f1, frames, labels, buttons), logo_icon