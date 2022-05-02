from tkinter import *
from tkinter import filedialog
import os


fenetre = Tk()
fenetre.title("Path")
fenetre.geometry("600x600")


dirname = ""

label = Label(fenetre, text=dirname)
label.pack()


def GetDir():
    global dirname
    dirname = filedialog.askdirectory()
    print(dirname)
    label.config(text=dirname)

def Save():
    with open(f"{os.path.dirname(__file__)}\\var.env", "w+", encoding="utf-8") as f:
        read = f.readlines()
        if dirname == " ":
            for line in read:
                if "DIR=" not in line:
                    f.write("DIR=")
        else:
            f.write(f"DIR={dirname}")
    fenetre.destroy()



bouton_getdir = Button(fenetre, text="Open", command=GetDir)
bouton_getdir.pack()

bouton_save = Button(fenetre, text="Save and Exit", command=Save)
bouton_save.pack()


fenetre.mainloop()