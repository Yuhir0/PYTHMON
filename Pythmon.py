#!/usr/bin/env python
# -*- coding: cp1252 -*-
#
# PYTHON
#
# Joc basat en Pokémon
# Els monstres els anomenarem Pythmons
#
# Per a que el joc funcioni correctamente, siusplau executa'l desde la carpeta PYTHMON
# Tambe hauras de tenir instal·lada una llibreria externa anomenada python-lxml
# que es fa servir per generar el fitxer xml amb les dades dels jugadors.
#
# Qualsevol dupte sobre el funcionament consulta el 'README' o be posat en contacte
# amb els propietaris del programa (Oscar Garcia, Daniel Gonzalo) IES Joan d'Àustria
#

import random, time, os

# Amb el següent podrem fer clear tant en windows com en linux
def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print "No es pot netegar la pantalla"

# Es l'apariencia de cada moment del joc (animacions)
def pantalla(text,escena):
    encombat0 = ""
    encombat1 = ""

    # Les dades dels pythmon que es mostraran, en cas de tenir efectes
    if encombat[0][0] != "":
        if encombat[0][10] != "N" and encombat[0][11] == "D":
            encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " | [" + encombat[0][10] + "] [" + encombat[0][11] + "]"
        elif encombat[0][10] != "N":
            encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " | [" + encombat[0][10] + "]"
        elif encombat[0][11] == "D":
            encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " | [" + encombat[0][11] + "]"
        else:
            encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " |"

        if encombat[1][10] != "N" and encombat[1][11] == "D":
            encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " | [" + encombat[1][10] + "] [" + encombat[1][11] + "]"
        elif encombat[1][10] != "N":
            encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " | [" + encombat[1][10] + "]"
        elif encombat[1][11] == "D":
            encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " | [" + encombat[1][11] + "]"
        else:
            encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " |"

    escriu = " "

    # Encara no hi ha combat, per tant hi ha una pantalla en negre i només es fa l'animació del text
    if escena == 0:
        for i in text:
            escriu += i
            print "\n\n\n\n\n\n\n\n\n"
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.03)
            clear()
        print "\n\n\n\n\n\n\n\n\n"
        print "+-----------------------------------------------------+"
        print escriu
        print "+-----------------------------------------------------+"

    # L'enemic treu un pythmon, animació de text + sortida al camp del pythmon
    elif escena == 1:
        for i in text:
            escriu += i
            clear()
            print "\n\n\n\n\n\n\n\n\n"
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.03)


        time.sleep(0.3)

        # Animació de quan el contrari treu un Pythmon
        for i in range(5):
            clear()
            for j in range(i):
                print "\t",
            print encombat1
            print "\n\n\n\n\n\n\n\n"
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.2)

    # El jugador treu un pythmon, animació de text + sortida al camp del pythmon
    elif escena == 2:
        for i in text:
            escriu += i
            clear()
            print "\t\t\t\t" + encombat1
            print "\n\n\n\n\n\n\n\n"
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.03)

        time.sleep(0.3)

        # Animació de quan el jugador treun un Pythmon
        for i in range(5,-1,-1):
            clear()
            print "\t\t\t\t" + encombat1
            print "\n\n\n\n\n\n\n"
            for j in range(i,0,-1):
                print "\t",
            print encombat0
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.2)

    # Quan surt el pythmon del contrari i el pyhtmon del jugador ja es a pista
    elif escena == 3:
        for i in text:
            escriu += i
            clear()
            print "\n\n\n\n\n\n\n\n"
            print encombat0
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.03)


        time.sleep(0.3)

        # Animació de quan el contrari treu un Pythmon
        for i in range(5):
            clear()
            for j in range(i):
                print "\t",
            print encombat1
            print "\n\n\n\n\n\n\n"
            print encombat0
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.2)

    # Els dos pythmon estan en combat, només es fa l'animació del text
    elif escena == 4:
        for i in text:
            escriu += i
            clear()
            print "\t\t\t\t" + encombat1
            print "\n\n\n\n\n\n\n"
            print encombat0
            print "+-----------------------------------------------------+"
            print escriu
            print "+-----------------------------------------------------+"
            time.sleep(0.03)


# Es defineixen els atacs
def Atac(tipus,potencia,atacant,defensor,torn,efecte):

    if potencia > 0:
        print "Potencia es mayro que 0"
        # Atacs molt efectius
        if tipus == "Planta" and defensor[1] == "Aigua" or tipus == "Foc" and defensor[1] == "Planta" or tipus == "Aigua" and defensor[1] == "Foc":
            mal = (potencia + atacant[3] - defensor[4]) * 2
            text = atacant[0] + " ha usat " + atacant[torn] + ", es molt efectiu."

        # Atacs poc efectius
        elif tipus == "Planta" and defensor[1] == "Foc" or tipus == "Foc" and defensor[1] == "Aigua" or tipus == "Aigua" and defensor[1] == "Planta":
            mal = (potencia + atacant[3] - defensor[4]) * 0.5
            text = atacant[0] + " ha usat " + atacant[torn] + ", no es gaire efectiu."

        # Atacs efectius
        else:
            mal = potencia + atacant[3] - defensor[4]
            text = atacant[0] + " ha usat " + atacant[torn] + "."


        if int(mal) < 1: # Si el atac es massa devil sempre fara com a minim 1 de mal
            pantalla(text, 3)
            defensor[2] -= 1
        elif random.randint(1,100) <= 5: # Si l'atac entra en el 5% farà el doble de mal (crític)
            pantalla(text + "\n Ha estat un cop critic", 3)
            defensor[2] -= int(mal) * 2
        else: # Un atac normal, sense ser molt devil ni critic
            pantalla(text, 3)
            defensor[2] -= int(mal)

    probabilitat = random.randint(1,100)

    # Efectes d'estat
    # Si el pythmon no és de foc, i no té cap efecte d'estat, es pot cremar.
    if efecte[0] == "C" and defensor[10] == "N" and defensor[1] != "Foc":
        if potencia == 0:
            pantalla(atacant[0] + " ha usat " + atacant[torn], 4)

        if efecte[1].isdigit():
            if probabilitat <= int(efecte[1:]):
                pantalla(defensor[0] + " s'ha cremat", 4)
                defensor[10] = "C"
        else:
            if probabilitat <= int(efecte[2:]):
                pantalla(defensor[0] + " s'ha cremat", 4)
                defensor[10] = "C"

    # Si el pythmon no té cap efecte d'estat, es pot paralitzar.
    elif efecte[0] == "P" and defensor[10] == "N":
        if probabilitat <= int(efecte[1:]):
            defensor[10] = "P"

    # Si el pythmon no té cap efecte d'estat, es pot dormir.
    elif efecte[0] == "S" and defensor[10] == "N":
        if potencia == 0:
            pantalla(atacant[0] + " ha usat " + atacant[torn], 4)

        if probabilitat <= int(efecte[1:]):
            defensor[10] = "S"

    # Efectes especials
    # Retrocés
    if "R" in efecte:
        if efecte[1].isdigit():
            if probabilitat <= int(efecte[1:]):
                return "R"
        else:
            if probabilitat <= int(efecte[2:]):
                return "R"

    # Drenadores
    elif efecte == "D":
        pantalla(atacant[0] + " ha usat " + atacant[torn], 4)
        defensor[11] = "D"

    # Drenatge
    elif efecte[0] == "G":
        atacant[2] += int(int(efecte[1:]) * mal / 100)
        if atacant[2] > atacant[12]:
            atacant[2] = atacant[12]

    return "N" # En cas de que no hi hagi retrocés

"""
Aqui estan tos els pythmon amb el seguient ordre [0]Nom, [1]Tipus, [2]Vida, [3]Atac, [4]Defensa, [5]Velocitat,
[6]Atac1, [7]Atac2, [8]Atac3, [9]Atac4, [10]Efecte d'estat, [11]Efecte especial ([10] & [11] N = cap efecte), [12]Vida Màxima.
"""
pythmon = [["Bulbasaur","Planta",231,147,134,126,"Fulla Afilada","Gigadrenatge","Placatge","Drenadores","N","N",231],
        ["Ivysaur","Planta",261,176,162,156,"Fulla Afilada","Gigadrenatge","Drenadores","Placatge","N","N",261],
        ["Venusaur","Planta",301,220,202,196,"Gigadrenatge","Raig Solar","Esporas","Dansa Espasa","N","N",301],
        ["Squirtle","Aigua",229,145,166,122,"Surf","Atac Rapid","Acua Jet","Placatge","N","N",229],
        ["Wartortle","Aigua",259,178,196,152,"Surf","Acua Jet","Cop Cos","Cascada","N","N",259],
        ["Blastoise","Aigua",299,222,236,192,"Surf","Hidrobomba","Cop Cos","Dansa Espasa","N","N",299],
        ["Charmander","Foc",219,154,122,166,"Llançaflames","Atac Rapid","Ullal Igni","Placatge","N","N",219],
        ["Charmeleon","Foc",257,180,152,196,"Llançaflames","Ullal Igni","Placatge","Dansa Espasa","N","N",257],
        ["Charizard","Foc",297,224,192,236,"Llançaflames","Flamarada","Hiper Raig","Dansa Espasa","N","N",297],
        ["Vulpix","Foc",217,129,116,166,"Llançaflames","Ullal Igni","Foc Fatuo","Atac Rapid","N","N",217],
        ["Ninetales","Foc",287,206,186,236,"Llançaflames","Foc Fatuo","Flamarada","Atac Rapid","N","N",287],
        ["Exeggcute","Planta",261,127,196,116,"Fulla Afilada","Gigadrenatge","Esporas","Placatge","N","N",261],
        ["Exeggutor","Planta",331,248,206,146,"Gigadrenatge","Esporas","Drenadores","Hiper Raig","N","N",331],
        ["Staryu","Aigua",201,138,146,206,"Surf","Atac Rapid","Acua Jet","Cascada","N","N",201],
        ["Starmie","Aigua",261,204,206,266,"Surf","Atac Rapid","Hidrobomba","Acua Jet","N","N",266],
        ["Magmar","Foc",271,248,150,222,"Llançaflames","Hiper Raig","Foc Fatuo","Flamarada","N","N",271],
        ["Tangela","Planta",271,160,266,156,"Gigadrenatge","Esporas","Drenadores","Raig Solar","N","N",271],
        ["Lapras","Aigua",401,226,196,156,"Surf","Cop Cos","Hidrobomba","Cascada","N","N",401],
        ["Magikarp","Aigua",999,999,999,1,"Perforador","Esquitxada","Esquitxada","Esquitxada","N","N",999]]

encombat=[[""],[""]]

""" Aquest petit block comproba si l'usuari te instal·lada la llibreria python-lxml
Tambe comprovem que el joc s'executa desdel directory PYTHMON per a que tot funcioni correctament """
if not "PYTHMON" in os.getcwd():
    pantalla("Per a poder jugar a aquest joc, siusplau executa'l des\n del directori PYTHMON sino el joc no s'iniciara'",0)
    exit()
elif os.name == "nt":
    os.system("dir C:\Python27\lib\site-packages\ >> registre.txt")
    lista = open("registre.txt","r")
    if not "lxml" in lista.read():
        pantalla("Per jugar a aquest joc es requereix d'una llibreria\n externa anomenada python-lxml.\n No podras jugar si no te la instal.les.",0)
        raw_input("Enter per continuar llegint")
        pantalla("Per instal.lar python-lxml pots anar al directori\n recursos de la carpet PYTHMON i selecciona un dels dos\n instal.lables. O be descarregau de la pagina oficial.",0)
        print lista.read()
        lista.close()
        os.system("del registre.txt")
        exit()
    lista.close()
    os.system("del registre.txt")

elif os.name == "posix":
    os.system("dpkg --get-selections | grep python-lxml > registre")
    xml = open("registre", "r")
    while not "python-lxml" in xml.read():
        pantalla("Per jugar a aquest joc es requereix d'una llibreria\n externa anomenada python-lxml.\n No podras jugar si no te la instal·les.",0)
        resposta = raw_input("Vols instal·lar-la? (s/N) ")
        if resposta.lower() == "s":
            clear()
            os.system("sudo apt install python-lxml -y")
        else:
            clear()
            pantalla("Adeu, fins un altre.",0)
            os.system("rm registre")
            exit()
        os.system("dpkg --get-selections | grep lxml > registre")
        xml = open("registre", "r")
        clear()
        if "python-lxml" in xml.read():
            pantalla("Gracies per instal·lar-la, hara ja pots jugar.",0)
            time.sleep(1.5)
    xml.close()
    os.system("rm registre")
from lxml import etree
#######################################################################################################################


mipythmon = [[""],[""],[""]] # Espai per als pythmon del jugador

# Abans d'iniciar el joc et demana un nom
pantalla("Quin es el tu nom?",0)
Nom = raw_input()

combat = 1 # Identifica la ronda per la que va el jugador

""" D'un fitxer xml agafem les dades i comprovem si el nom que ha introduit
l'usuari hi es, per tal de continuar la partida guardada o començar una nova """
partida = etree.parse('partida.xml') # Carreguem el fixer 'partida.xml' que conté les dades dels jugadors
jugadors = partida.findall("jugador") # Trobem tots el jugadors

lj = len(jugadors) # Averigüem quants jugadors són

for i in range(lj):
    if Nom == jugadors[i].attrib["nom"]:
        numj = i # Guardara la pocicio del jugador a la llista
        print "Tens una partida començada"
        p = jugadors[i].findall("pythmon") # Trobem tots els pythmon si el jugador esta registrat

        for n in range(3):
            mipythmon[n] = pythmon[int(p[n].attrib["num"])]
        combat = int(jugadors[i].find("combat").attrib["cont"]) # El convertim a enter i li assignem a combat
        break
    elif i == lj-1 and Nom != jugadors[lj-1].attrib["nom"]:
        print "Benvingut a la nostra torre Pythmon, guanya tots entrenadors i aconsegueix la victoria"

if combat > 10: # Si el jugador te mes de 10 combats ja el ha fet tots
    exit()
if combat > 1 and combat < 10: # Si el jugador ha fet més d'un combat indicara la ronda y pasara al while del joc.
    print "Vas per la ronda",combat

else:
    # Formulem el xml per inscriure un nou jugador
    save = partida.getroot()
    noujugador = etree.Element("jugador", nom=Nom)
    save.append(noujugador)

    # Llista els pythmon en dos columnes per a que el jugador els pugui veure
    for i in range(9):
        print str(i)+")",pythmon[i][0],"\t",
        print str(9 + i) + ")",pythmon[9 + i][0]

    # Demana al jugador que esculli 3 pythmon i els guarda
    for i in range(3):
        escull = int(input("Escull el teu " + str(i + 1) + " pythmon: "))
        mipythmon[i] = pythmon[escull][:]

        # Registrem els pythmon en format xml
        p = etree.Element("pythmon", num=str(escull))
        noujugador.append(p)

    # Mostra els pythmon escollits pel jugador
    for i in range(3):
            print mipythmon[i][0]

    # Guardem en format xml els combats
    cont = etree.Element("combat", cont=str(combat))
    noujugador.append(cont)
    jugadors = partida.findall("jugador")
    numj = len(jugadors) - 1

# Guardem totes les dades formulades del xml al fitxer 'partida.xml'
partida.write('partida.xml')

time.sleep(2.5)

contrari = [[""],[""],[""]] # Espai per als pythmon del oponent

# Aquí tenim la llista amb els noms dels entrenadors rivals
entrenadors = ["Marcos","Ana","Marta","Tarazona","teu oponent","Joan","David","Paula","Carles","Sergi","Pablo","Wenceslau","Nacho","Amelia","Joaquim","Arantxa","Alvaro"]


# Aquí es desenvolupa la major part del joc.
while combat <= 10:
    clear()

    son = [4,4] # Serveix per si el pythmon te l'efecte de son'

    # S'escullen els Pythmon del contrari
    for i in range(3):
        rnd = random.randint(0,17)
        contrari[i] = pythmon[rnd][:]

    rotacio = 0
    encombat[0] = mipythmon[0]
    encombat[1] = contrari[rotacio] # Cada cop que es mori un pythmon el contrari canviara al següent

    # Faig que la variable joy tingui les dades dels pythmon del jugador per més endevant
    joy = []
    for i in mipythmon:
        joy.append(i[:])

    entrenador = random.randint(0,16)

    # Comença la animació del principi del combat
    pantalla(Nom + " el teu oponent sera en " + entrenadors[entrenador], 0)
    time.sleep(2)
    pantalla(entrenadors[entrenador] + " a tret a " + encombat[1][0],1)
    time.sleep(1)
    pantalla("Has tret a " + encombat[0][0], 2)
    time.sleep(1)

    # Acaba la animació d'inici del combat.
    while True:
        pantalla("Fes el teu moviment", 3)
        if len(encombat[0][6]) < 5:
            print "1) " + encombat[0][6] + "\t\t 2) " + encombat[0][7] + "\t 5)Pythmon"
        elif len(encombat[0][6]) > 12:
            print "1) " + encombat[0][6] + " 2) " + encombat[0][7] + "\t 5)Pythmon"
        else:
            print "1) " + encombat[0][6] + "\t 2) " + encombat[0][7] + "\t 5)Pythmon"

        if len(encombat[0][8]) < 6:
            print "3) " + encombat[0][8] + "\t\t 4) " + encombat[0][9]
        elif len(encombat[0][8]) > 12:
            print "3) " + encombat[0][8] + " 4) " + encombat[0][9]
        else:
            print "1) " + encombat[0][8] + "\t 4) " + encombat[0][9]

        juga = int(input())
        if juga == 5:
            pantalla("Escull pythmon: ", 4)
            for i in range(3):
                print str(i+1) + ") " + mipythmon[i][0]
            escull = int(input())

            # Controla que la informació introduida sigui correcte i no pugui canviar a un pythmon que esta devilitat
            while escull < 1 or escull > 3 or mipythmon[escull - 1][2] < 1:
                if mipythmon[escull - 1][2] < 1:
                    pantalla("No pots treure un Pyhtmon devilitat", 4)
                else:
                    pantalla("No tenim aquesta opcio, introdueix un valor correcte", 4)

                for i in range(3):
                    print str(i+1) + ") " + mipythmon[i][0]

                escull = int(input())

            encombat[0] = mipythmon[escull - 1]

        cops = 0
        while cops < 2:
            torn = 0
            fst = 0
            snd = 0
            if juga > 0 and torn < 5 and encombat[0][5] > encombat[1][5]: # Si el jugador ataca i es més ràpid que l'enemic, atacarà primer.
                if cops == 0:
                    fst = 0
                    snd = 1
                    torn = juga
                else:
                    torn = random.randint(1,4)
                    fst = 1
                    snd = 0
            elif juga > 0 and torn < 5 and encombat[0][5] < encombat[1][5]: # Si el jugador ataca i es més lent que l'enemic, atacarà segon.
                if cops == 0:
                    fst = 1
                    snd = 0
                    torn = random.randint(1,4)
                else:
                    fst = 0
                    snd = 1
                    torn = juga
            elif juga > 4:
                fst = 1
                snd = 0
                cops = 2
                torn = random.randint(1,4)

            # Pythmon adormit
            if encombat[fst][10] == "S":
                if random.randint(0,4) == 0 or son[fst] == 0: # Si es 0 de entr 0 - 4 o ya han pasat 4 torns es desperta
                    encombat[fst][10] = "N"
                    son[fst] = 4
                    pantalla(encombat[fst][0] + " s'ha despertat!", 4)
                    time.sleep(1)
                else: # Si no es desperta se li resta 1 al temps de estar dormit
                    pantalla(encombat[fst][0] + " està dormit, no pot atacar!", 4)
                    son[fst] -= 1
                    time.sleep(1)

            # Els Atacs
            if encombat[fst][10] == "P" and random.randint(0,2) == 0:
                pantalla(encombat[fst][0] + " està paralitzat, no pot atacar!", 4)
            elif encombat[fst][10] != "S": # Si el pythmon esta adormit no pot atacar
                retroces = "N"
                if encombat[fst][torn + 5] == "Llançaflames":
                    retroces = Atac("Foc", 90,encombat[fst],encombat[snd],torn + 5,"C10")
                elif encombat[fst][torn + 5] == "Flamarada":
                    retroces = Atac("Foc", 120,encombat[fst],encombat[snd],torn + 5,"C30")
                elif encombat[fst][torn + 5] == "Ullal Igni":
                    retroces = Atac("Foc", 65,encombat[fst],encombat[snd],torn + 5,"CR10")
                elif encombat[fst][torn + 5] == "Foc Fatuo":
                    retroces = Atac("Foc", 0,encombat[fst],encombat[snd],torn + 5,"C100")
                elif encombat[fst][torn + 5] == "Surf":
                    retroces = Atac("Aigua", 90,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Hidrobomba":
                    retroces = Atac("Aigua", 110,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Acua Jet":
                    retroces = Atac("Aigua", 40,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Cascada":
                    retroces = Atac("Aigua", 80,encombat[fst],encombat[snd],torn + 5,"R30")
                elif encombat[fst][torn + 5] == "Gigadrenatge":
                    retroces = Atac("Planta", 80,encombat[fst],encombat[snd],torn + 5,"G30")
                elif encombat[fst][torn + 5] == "Fulla Afilada":
                    retroces = Atac("Planta", 70,encombat[fst],encombat[snd],torn + 5,"R10")
                elif encombat[fst][torn + 5] == "Raig Solar":
                    retroces = Atac("Planta", 120,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Esporas":
                    retroces = Atac("Planta", 0,encombat[fst],encombat[snd],torn + 5,"S100")
                elif encombat[fst][torn + 5] == "Drenadores":
                    retroces = Atac("Planta", 0,encombat[fst],encombat[snd],torn + 5,"D")
                elif encombat[fst][torn + 5] == "Placatge":
                    retroces = Atac("Normal",40,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Atac Rapid":
                    retroces = Atac("Normal",40,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Cop Cos":
                    retroces = Atac("Normal",85,encombat[fst],encombat[snd],torn + 5,"P30")
                elif encombat[fst][torn + 5] == "Dansa Espasa":
                    retroces = Atac("Normal",0,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Perforador":
                    retroces = Atac("Normal",9999,encombat[fst],encombat[snd],torn + 5,"N")
                elif encombat[fst][torn + 5] == "Hiper Raig":
                    retroces = Atac("Normal",150,encombat[fst],encombat[snd],torn + 5,"N")

                # Quan es devilita el pythmon, s'acaba la ronda d'atacs
                if encombat[0][2] < 1:
                    encombat[0][2] = 0
                    cops = 2

                if encombat[1][2] < 1:
                    encombat[1][2] = 0
                    cops = 2

                # Si un dels pythmon retrocedeix
                if retroces == "R" and cops == 0 and encombat[snd][2] > 0: # Si retroces es igual a 'R' vol dir que el pythmon retrocedira
                    time.sleep(1)
                    pantalla(encombat[snd][0] + " ha retrocedit", 4)
                    cops = 2

                time.sleep(1)

            cops += 1

        time.sleep(1)

        # Cremada
        if encombat[0][10] == "C": # Si el pythmon del jugador cremat
            pantalla(encombat[0][0] + " a rebut mal per la cremada", 4)
            encombat[0][2] -= int(encombat[0][12] * 0.1)
            time.sleep(1)

        if encombat[1][10] == "C": # Si el pythmon del contrari esta cremat
            pantalla(encombat[1][0] + " a rebut mal per la cremada", 4)
            encombat[1][2] -= int(encombat[1][12] * 0.1)
            time.sleep(1)


        # Drenadoras
        if encombat[0][11] == "D": # Si el pythmon del jugador te drenadoras
            pantalla(encombat[1][0] + " ha drenat vida de "  + encombat[0][0], 4)
            encombat[0][2] -= int(encombat[0][12] * 0.125)
            encombat[1][2] += int(encombat[0][12] * 0.125)
            if encombat[1][2] > encombat[1][12]:
                encombat[1][2] = encombat[1][12]
            if encombat[0][2] < 1:
                encombat[0][2] = 0
            time.sleep(1)

        if encombat[1][11] == "D": # Si el pythmon del contrari te drenadoras
            pantalla(encombat[0][0] + " ha drenat vida de "  + encombat[1][0], 4)
            encombat[1][2] -= int(encombat[1][12] * 0.125)
            encombat[0][2] += int(encombat[1][12] * 0.125)
            if encombat[0][2] > encombat[1][12]:
                encombat[0][2] = encombat[1][12]
            if encombat[1][2] < 1:
                encombat[1][2] = 0
            time.sleep(1)


        # Si es devilita tot l'equip del contrari
        if contrari[2][2] < 1:
            encombat[1][2] = 0
            pantalla(encombat[1][0] + " s'ha devilitat",4)
            time.sleep(1)
            pantalla("Has guanyat el combat",0)
            time.sleep(2)
            break

        # Si es devilita un pythmon del contrari
        elif encombat[1][2] < 1:
            encombat[1][2] = 0
            pantalla(encombat[1][0] + " s'ha devilitat",4)
            rotacio += 1
            encombat[1] = contrari[rotacio]
            time.sleep(0.5)
            pantalla(entrenadors[entrenador] + " a tret a " + encombat[1][0],3)

       # Si es devilita un pythmon del jugador
        if encombat[0][2] < 1:
            pantalla("Escull pythmon: ", 4)
            for i in range(3):
                print str(i+1) + ") " + mipythmon[i][0]
            escull = int(input())

            # Controla que la informació introduida sigui correcte i no pugui canviar a un pythmon que esta devilitat
            while escull < 1 or escull > 3 or mipythmon[escull - 1][2] < 1:
                if mipythmon[escull - 1][2] < 1:
                    pantalla("No pots triar un pythmon devilitat", 4)
                else:
                    pantalla("Siusplau, introdueix un numero correcte: ", 4)

                for i in range(3):
                    print str(i+1) + ") " + mipythmon[i][0]

                escull = int(input())

            encombat[0] = mipythmon[escull - 1]

        # Si es devilita tot l'equip del jugador
        if mipythmon[0][2] < 1 and mipythmon[1][2] < 1 and mipythmon[2][2] < 1:
            pantalla("Has perdut",0)
            combat = 10
            break

        clear()

    combat += 1

    # Agafem el jugador actual i li guardem la ronda per la que va
    jugadors[numj].find("combat").attrib["cont"]=str(combat)

    # Guardem totes les dades formulades del xml al fitxer 'partida.xml'
    partida.write('partida.xml')

    # Amb això faig que les estadístiques dels pythmon de l'usuari tornin a l'estat original
    mipythmon = []
    for i in joy:
        mipythmon.append(i[:])
