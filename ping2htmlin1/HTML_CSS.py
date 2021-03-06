from os import listdir

class HTML_CSS:
    def fCSS():
        return('''

body
{
    background-color: #2b2b2b;
    color: #ffffff;
    font-family: "Courier New", Courier, monospace;
    font-size: 12px;
    text-align: center;
}

p
{
    font-size: 12px;
}

header
{
    position: absolute;
    font-size: 11px;
    font-family:'Arial Narrow Bold', sans-serif;
    width: 40%;
    left: 30%;
    top: 0px;
    height: 15%;
    background-color: #0051ad;
    direction: ltr;
    overflow: auto;
}
nav
{
    position: absolute;
    color: #fff;
    width: 30%;
    top: 0px;
    left: 0%;
    height: 100%;
    background-color: rgb(34, 46, 46);
    z-index: 100;

    direction: ltr;
    overflow: auto;
}
nav h2
{
    padding-left: 10px;
}
  
nav a
{
    font-size: 14px;
    color: #fff;
    display: block;
    padding: 12px;
    padding-left: 5%;
    text-decoration: none;
    outline: none;
}
nav a:hover
{
    color: #386aff;
    background: #fff;
    position: relative;
    background-color: #fff;
    border-top-right-radius: 22px;
    border-bottom-right-radius: 22px;
}

nav .current
{
    background-color: #386aff;
    color: white;
    border-top-right-radius: 22px;
    border-bottom-right-radius: 22px;
}

.display
{
    position: absolute;
    top: 0px;
    right: 0px;
    width: 30%;
    height: 15%;
    background-color: #2b2b2b;
    z-index: 100;
    direction: ltr;
    overflow: auto;
}

.display h2
{
    padding-top: 0px;
    font-size: 17px;
}

.bilan
{
    position: absolute;
    width: 70%;
    left: 30%;
    height: 25%;
    top: 15%;
    background-color: #5a86ff;
    direction: ltr;
    overflow: auto;
}
.bilan:hover {
    color: #83fbff;
}

.list_container
{
    position: absolute;
    width: 70%;
    left: 30%;
    top: 40%;
    height: 60%;
    direction: ltr;
    overflow: auto;

}

.container
{
    position: absolute;
    width: 100%;
    z-index: 100;
}

.coupure:hover {
    color: #c27efa;
}


.colorcontainer
{
    position: absolute;
    height: auto;
    width: 100%;
}

.blue
{
    height: 65px;
    background-color: #386aff;
    z-index: 110;
}

.cyan
{
    height: 65.5px;
    background-color: #0051ad;
    z-index: 110;
}

.list_container::-webkit-scrollbar {
    width: 12px;
}
 
.list_container::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    border-radius: 10px;
}
 
.list_container::-webkit-scrollbar-thumb {
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    background-color: #0051ad;
}


.display::-webkit-scrollbar {
    width: 12px;
}
 
.display::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    border-radius: 10px;
}
 
.display::-webkit-scrollbar-thumb {
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    background-color: #0051ad;
}


header::-webkit-scrollbar {
    width: 12px;
}
 
header::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    border-radius: 10px;
}
 
header::-webkit-scrollbar-thumb {
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    background-color: #0051ad;
}


nav::-webkit-scrollbar {
    width: 12px;
}
 
nav::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    border-radius: 10px;
}
 
nav::-webkit-scrollbar-thumb {
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5);
    background-color: #0051ad;
}


.bilan::-webkit-scrollbar {
    width: 12px;
}
 
.bilan::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5); 
    border-radius: 10px;
}
 
.bilan::-webkit-scrollbar-thumb {
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0, 136, 255, 0.5);
    background-color: #0051ad;
}''')

    def fHTML(heuredebuttest, heurefintest, dureetest, nombrecoupures, dureecoupures, moyennecoupures, totalcoupures, heurefintestchange, totalcolorcontainer, directory):
        Fichtexte = f'''<nav><h2>Navigation:</h2>'''
        i = 0
        for fichiers in listdir(directory):
            if fichiers.endswith(".html") and fichiers.startswith("docping---"):
                if "en_cours" in fichiers:
                    heurefintestchange2 = f'{heurefintestchange}'.replace("_", "<br>")
                    Fichtexte = Fichtexte + f'''<a class="current", href="docping---{heurefintestchange}.html">{heurefintestchange2}</a>'''
                else:
                    fichiersnohtml = fichiers.replace(".html", "")
                    fichiersnohtml = fichiersnohtml.replace("docping---", "")
                    fichiersnohtml = fichiersnohtml.replace("_", "<br>")
                    Fichtexte = Fichtexte + f'''<a href="{fichiers}">{fichiersnohtml}</a>'''
        Fichtexte = Fichtexte + f'''</nav>
'''

        for fichiers in listdir(directory):
            stop=False
            if fichiers.endswith(".html") and fichiers.startswith("docping---"):
                if "en cours" in fichiers:
                    pass
                else:
                    with open(f"{directory}\\{fichiers}", "r", encoding="utf-8") as fichier:
                        contenu = fichier.readlines()
                    
                    for ligne in contenu:
                        i = i + 1
                        if "<nav>" in ligne and stop==False:
                            try:
                                contenu[i-1] = Fichtexte
                                stop=True
                            except:
                                print(len(contenu))
                    i = 0
                    
                    with open(f"{directory}\\{fichiers}", "w", encoding="utf-8") as fichier:
                        fichier.writelines(contenu)


        fichiers2 = f"docping---{heurefintestchange}.html"
        fichiersbr = f"{fichiers2}".replace("_", "_<br>")
        return(f'''
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet"href="docping.css">
        <title>Ping</title>
    </head>
    <body>
{Fichtexte}
        <header>
            <h1>R??sultats du test de coupures<br>de connection</h1>
        </header>
        <div class="display">
            <h2>{fichiersbr}</h2>
        </div>
        <div class="bilan">
            <p>
            <strong>D??but du test:</strong> {heuredebuttest}<br>
            <strong>Fin du test:</strong> {heurefintest}<br>
            <strong>Dur??e du test:</strong> {dureetest}<br><br>
            <strong>Nombre de coupures:</strong> {nombrecoupures}<br>
            <strong>Dur??e totale des coupures:</strong> {dureecoupures}<br>
            <strong>Dur??e moyenne des coupures:</strong> {moyennecoupures}
            </p>
        </div>
        <div class="list_container">
            <div class="colorcontainer">
                {totalcolorcontainer}
            </div>
            <div class="container">
                {totalcoupures}
            </div>
        </div>
    </body>
</html>
''')


    def currentHTML(directory):
        for fichiers in listdir(directory):
            i=0
            contenu = ""
            lignesplit = ""
            lignejoin = ""
            if fichiers.endswith(".html") and fichiers.startswith("docping---"):
                if "en cours" in fichiers:
                    pass
                else:
                    with open(f"{directory}\\{fichiers}", "r", encoding="utf-8") as fichier:
                        contenu = fichier.readlines()
                        j=0
                        for ligne in contenu:
                            i = i + 1
                            if "<nav>" in ligne:
                                ligne = ligne.replace('class="current",', "")
                                lignesplit = ligne.split()
                                stop = False
                                j = 0
                                for item in lignesplit:
                                    j = j + 1

                                    fichierpath2 = f'{directory}'.replace('\\', '\\\\')
                                    changefichier = f"{fichier}"
                                    changefichier = f"{changefichier}".replace(f"<_io.TextIOWrapper name='","")
                                    changefichier = f"{changefichier}".replace(f"{fichierpath2}\\\\", "")
                                    changefichier = f"{changefichier}".replace("' mode='r' encoding='utf-8'>","")

                                    if f"{changefichier}" in item and stop == False:

                                        stop = True
                                        l = i
                                        lignesplit.insert(j-1, 'class="current",')

                        if lignesplit != None:
                            lignejoin = " ".join(lignesplit)
                            contenu[l-1] = lignejoin + "\n"
                            i = 0
                            l = 0
                        with open(f"{directory}\\{fichiers}", "w", encoding="utf-8") as fichier:
                            if contenu != []:
                                fichier.writelines(contenu)
