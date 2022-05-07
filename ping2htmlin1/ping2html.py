from os import path, getenv, listdir, system, rename
from tkinter import Tk, Button, Label
from time import strftime, sleep
from datetime import datetime
from threading import Thread
from HTML_CSS import HTML_CSS
from ChangeHTMLFolder import Shortcutmenu, GetDir, Save
from dotenv import load_dotenv

exit=False
numberFichier = 1
totalcoupures = ""
file = __file__


def ftkinter():
    global gui_ping
    gui_ping = Tk()
    btn = Button(gui_ping, text ="Exit", command = fexit)
    btn.pack()
    Thread(target=prg).start()
    gui_ping.mainloop()

def fexit():
    global exit
    exit=True
    menudestroy()
    return exit

def prg():
    global numberFichier, totalcoupurest, directory
    load_dotenv(f'{path.dirname(__file__)}\\.env')
    load_dotenv(verbose=True)
    dir = getenv('DIR')
    print(dir)
    if dir == None or dir == "" or dir == " ":
        directory = f"{path.dirname(__file__)}"
    else:
        directory = dir
    var=True
    totalcoupurest = ""
    totalcolorcontainer = ""
    for fichier in listdir(path.dirname(__file__)):
        if "docping---en_cours.html" in fichier:
            fichier = open(f"{directory}\\docping---en_cours.html", "r+", encoding="utf-8")
        else:
            fichier = open(f"{directory}\\docping---en_cours.html", "w", encoding="utf-8")
            fichier.close()
            fichier = open(f"{directory}\\docping---en_cours.html", "r+", encoding="utf-8")


    fichier.truncate(0)
    heuredebuttest = datetime.now()
    dureecoupures = 0
    nombrecoupures = 0
    color = "blue"
    height= ""
    while exit == False:
        sleep(0.1)
        response = system("ping -n 1 google.com")
        a = datetime.now()
        heure = strftime(a.strftime("%Y-%m-%d %H:%M:%S"))

        if response == 1 and var == True:
            
            heuredebut=a
            totalcoupures1 = f'<div><p class="coupure haut"><strong>Début de coupure:</strong> {heure}<br>'
            var=False

        if response == 0 and var == False:
            heurefin=datetime.now()

            if dureecoupures == 0:
                dureecoupures = heurefin - heuredebut
            else:
                dureecoupures = dureecoupures + (heurefin - heuredebut)
            totalcoupures2 = f'<strong>Fin de coupure:</strong> {heure}</p><p class="coupure"><strong>Durée de coupure:</strong> {str(heurefin - heuredebut)}</p></div>'
            if color == "blue":
                color = "cyan"
            else:
                color = "blue"
            if height == "":
                height = "haut"
            else:
                height = ""
            totalcoupurest = totalcoupurest + totalcoupures1 + totalcoupures2
            totalcolorcontainer = totalcolorcontainer + f'<div class="{color}"></div>'
            nombrecoupures += 1
            var=True
    dureetest = datetime.now() - heuredebuttest
    if nombrecoupures != 0:
        moyennecoupures = dureecoupures/nombrecoupures
    else:
        moyennecoupures = "0"
    heurefintest = datetime.now()
    heurefintestchange = heurefintest.strftime("%Y-%m-%d_%H-%M-%S")
    fichier.write(HTML_CSS.fHTML(heuredebuttest, heurefintest, dureetest, nombrecoupures, dureecoupures, moyennecoupures, totalcoupurest, heurefintestchange, totalcolorcontainer, directory))
    fichier.close()

    rename(f"{directory}\\docping---en_cours.html", f"{directory}\\docping---{heurefintestchange}.html")
    HTML_CSS.currentHTML(directory)
    system(f'start "" "{directory}\\docping---{heurefintestchange}.html"')


def css():
    with open(f"{directory}\\docping.css", "w+", encoding="utf-8") as fcss:
        fcss.truncate(0)
        fcss.write(HTML_CSS.fCSS())


def GetDirInput():
    GetDir(label)
def SaveInput():
    Save()
    fenetre.destroy()
    menu()



def tkHTMLMenu():
    global label, dirname, fenetre

    fenetre = Tk()
    fenetre.title("Path")
    fenetre.geometry("600x600")


    dirname = ""

    label = Label(fenetre, text=dirname)
    label.pack()

    bouton_getdir = Button(fenetre, text="Open", command=GetDirInput)
    bouton_getdir.pack()

    bouton_save = Button(fenetre, text="Save and Exit", command=SaveInput)
    bouton_save.pack()

    bouton_ping = Button(fenetre, text="Add shortcut for ping2html", command=Shortcutmenu)
    bouton_ping.pack()


    fenetre.mainloop()



def exitping():
    gui_menu.destroy()
    ftkinter()
    css()

def menudestroy():
    gui_ping.destroy()

def tkHTMLMenuinput():
    gui_menu.destroy()
    tkHTMLMenu()

def menu():
    global gui_menu

    gui_menu = Tk()
    gui_menu.title("Path")
    gui_menu.geometry("600x600")


    bouton_menu = Button(gui_menu, text="Change HTML Folder", command=tkHTMLMenuinput)
    bouton_menu.pack()

    bouton_ping = Button(gui_menu, text="Launch Ping", command=exitping)
    bouton_ping.pack()

    bouton_exit = Button(gui_menu, text="Exit", command=gui_menu.destroy)
    bouton_exit.pack()


    gui_menu.mainloop()

menu()