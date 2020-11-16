from tkinter import *
import tkinter.ttk
from PIL import ImageTk, Image

dark_blue = "#0E0C24"
light_green = "#0BFB2E"
light_dark_blue = "#46417F"
blue = "#112AE5"
grey = "#C5B5B5"
white = "#FFFFFF"
black = "#000000"

def logo_reshape(x, y):
    logo_icon = Image.open('Images\PMA_Icon.png')
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