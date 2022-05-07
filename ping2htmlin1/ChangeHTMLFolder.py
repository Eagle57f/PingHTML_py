from tkinter import filedialog, Label, Tk, Button
from os import path
from winshell import desktop, CreateShortcut

dirname = ""

def Shortcutmenu():
    CreateShortcut(
        Path=path.join(desktop(), "Launch ping2html menu.lnk"),
        Target=f"{path.dirname(__file__)}\\menu.exe",
        Description="Launch ping2html menu"
    )


def GetDir(label):
    global dirname
    dirname = filedialog.askdirectory()
    print(dirname)
    label.config(text=dirname)

def Save():
    global dirname
    with open(f"{path.dirname(__file__)}\\.env", "w+", encoding="utf-8") as f:
        read = f.readlines()
        if dirname == " ":
            for line in read:
                if "DIR=" not in line:
                    f.write("DIR=")
        else:
            f.write(f"DIR={dirname}")
