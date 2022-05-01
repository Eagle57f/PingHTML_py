import os, tkinter
from time import strftime, sleep
from datetime import datetime
from threading import Thread
from HTML_CSS import HTML_CSS

exit=False
numberFichier = 1
totalcoupures = ""
file = __file__

def ftkinter():
    global gui
    gui = tkinter.Tk()
    btn = tkinter.Button(gui, text ="Exit", command = fexit)
    btn.pack()
    Thread(target=prg).start()
    gui.mainloop()

def fexit():
    global exit
    exit=True
    gui.destroy()
    return exit

def prg():
    global numberFichier, totalcoupurest
    var=True
    totalcoupurest = ""
    totalcolorcontainer = ""
    for fichier in os.listdir(os.path.dirname(__file__)):
        if "docping---en_cours.html" in fichier:
            fichier = open(f"{os.path.dirname(__file__)}\\docping---en_cours.html", "r+", encoding="utf-8")
        else:
            fichier = open(f"{os.path.dirname(__file__)}\\docping---en_cours.html", "w", encoding="utf-8")
            fichier.close()
            fichier = open(f"{os.path.dirname(__file__)}\\docping---en_cours.html", "r+", encoding="utf-8")

    fichierpath = os.path.dirname(__file__)
    fichier.truncate(0)
    heuredebuttest = datetime.now()
    dureecoupures = 0
    nombrecoupures = 0
    color = "blue"
    height= ""
    while exit == False:
        sleep(0.1)
        response = os.system("ping -n 1 google.com")
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
    fichier.write(HTML_CSS.fHTML(heuredebuttest, heurefintest, dureetest, nombrecoupures, dureecoupures, moyennecoupures, totalcoupurest, heurefintestchange, totalcolorcontainer))
    fichier.close()

    os.rename(f"{fichierpath}\\docping---en_cours.html", f"{fichierpath}\\docping---{heurefintestchange}.html")
    HTML_CSS.currentHTML(fichierpath)
    os.system(f'start "" "docping---{heurefintestchange}.html"')





ftkinter()

def css():
    with open(f"{os.path.dirname(__file__)}\\docping.css", "w+", encoding="utf-8") as fcss:
        fcss.truncate(0)
        fcss.write(HTML_CSS.fCSS())


css()