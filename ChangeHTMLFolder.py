from tkinter import filedialog, Label, Tk, Button
from os import path
from winshell import desktop, CreateShortcut

def ShortcutFolder():
    CreateShortcut(
        Path=path.join(desktop(), "Change HTML Folder.lnk"),
        Target=f"{path.dirname(__file__)}\\ChangeHTMLFolder.exe",
        Description="Change HTML Folder"
    )

def ShortcutPing():
    CreateShortcut(
        Path=path.join(desktop(), "Launch ping2html.lnk"),
        Target=f"{path.dirname(__file__)}\\ping2html.exe",
        Description="Launch ping2html"
    )


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
    with open(f"{path.dirname(__file__)}\\.env", "w+", encoding="utf-8") as f:
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

bouton_folder = Button(fenetre, text="Add shortcut for ChangeHTMLFolder", command=ShortcutFolder)
bouton_folder.pack()

bouton_ping = Button(fenetre, text="Add shortcut for ping2html", command=ShortcutPing)
bouton_ping.pack()


fenetre.mainloop()