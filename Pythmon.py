#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PYTHON  
# 
# Joc basat en Pokémon 
# Els monstres els anomenarem Pythmons
#
import random
import time
import os
from lxml import etree


# Amb el següent podrem fer clear tant en windows com en linux
def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        raise "No es pot netegar la pantalla"
        print  "<-No s'ha pogut netejar la pantalla->"

""" 
Aqui estan tos els pythmon amb el seguient ordre Nom, Tipus, Vida, Atac, Defensa,
Velocitat, Atac1, Atac2, Atac3.
"""
pythmon = [["Bulbasaur","Planta",231,147,134,126],
		["Ivysaur","Planta",261,176,162,156],
		["Venusaur","Planta",301,220,202,196,"Gigadrenatge"],
		["Squirtle","Aigua",229,145,166,122],
		["Wartortle","Aigua",259,178,196,152],
		["Blastoise","Aigua",299,222,236,192,"Surf"],
		["Charmander","Foc",219,154,122,166],
		["Charmeleon","Foc",257,180,152,196,],
		["Charizard","Foc",297,224,192,236,"Llançaflames"],
		["Vulpix","Foc",217,129,116,166],
		["Ninetales","Foc",287,206,186,236],
		["Exeggcute","Planta",261,127,196,116],
		["Exeggutor","Planta",331,248,206,146],
		["Staryu","Aigua",201,138,146,206],
		["Starmie","Aigua",261,204,206,266],
		["Magmar","Foc",271,248,150,222],
		["Tangela","Planta",271,160,266,156],
		["Lapras","Aigua",401,226,196,156],
		["Magikarp","Aigua",999,999,999,1]]

# Es l'apariencia de cada moment del joc.
def pantalla(text,escena):
	escriu = " "
	if escena == 0:
		for i in text:
			escriu += i
			print "\n\n\n\n\n\n\n"
			print "+-----------------------------------------------+"
			print escriu
			print "+-----------------------------------------------+"
			time.sleep(0.05)
			clear()
		print "\n\n\n\n\n\n\n"
		print "+-----------------------------------------------+"
		print "",text
		print "+-----------------------------------------------+"
		
	elif escena == 1:
		for i in text:
			escriu += i
			clear()
			print "\n\n\n\n\n\n\n"
			print "+-----------------------------------------------+"
			print escriu
			print "+-----------------------------------------------+"
			time.sleep(0.05)
			
		
		time.sleep(0.3)
			
		for i in range(4):
			clear()
			for j in range(i):
				print "\t",
			print encombat[1][0] + " | vida:",encombat[1][2]
			print "\n\n\n\n\n\n"
			print "+-----------------------------------------------+"
			print " " + text
			print "+-----------------------------------------------+"
			time.sleep(0.2)
	
	elif escena == 2:	
		for i in text:
			escriu += i
			clear()
			print "\t\t\t" + encombat[1][0] + " | vida:",encombat[1][2]
			print "\n\n\n\n\n\n"
			print "+-----------------------------------------------+"
			print escriu
			print "+-----------------------------------------------+"
			time.sleep(0.05)
		
		time.sleep(0.3)
		
		for i in range(5,-1,-1):
			clear()
			print "\t\t\t" + encombat[1][0] + " | vida:",encombat[1][2]
			print "\n\n\n\n\n"
			for j in range(i,0,-1):
				print "\t",
			print encombat[0][0] + " | vida:",encombat[0][2]
			print "+-----------------------------------------------+"
			print " " + text
			print "+-----------------------------------------------+"
			time.sleep(0.2)
	
	elif escena == 3:
		for i in text:
			escriu += i
			clear()
			print "\t\t\t" + encombat[1][0] + " | vida:",encombat[1][2]
			print "\n\n\n\n\n"
			print encombat[0][0] + " | vida:",encombat[0][2]
			print "+-----------------------------------------------+"
			print escriu
			print "+-----------------------------------------------+"
			time.sleep(0.05)


# Es defineixen els atacs
def Atac(tipus,potencia,encombat,torn):	
	if tipus == "Planta" and encombat[1][1] == "Aigua" or tipus == "Foc" and encombat[1][1] == "Planta" or tipus == "Aigua" and encombat[1][1] == "Foc":
		mal = (potencia + encombat[0][3] - encombat[1][4]) * 2
		pantalla(encombat[0][0] + " ha usat " + encombat[0][torn] + ", es molt efectiu.", 3)
		
	elif tipus == "Planta" and encombat[1][1] == "Foc" or tipus == "Foc" and encombat[1][1] == "Aigua" or tipus == "Aigua" and encombat[1][1] == "Planta":
		mal = (potencia + encombat[0][3] - encombat[1][4]) * 0.5
		pantalla(encombat[0][0] + " ha usat " + encombat[0][torn] + ", no es gaire efectiu.", 3)
		
	else:
		mal = potencia + encombat[0][3] - encombat[1][4]
		pantalla(encombat[0][0] + " ha usat " + encombat[0][torn] + ".", 3)
	encombat[1][2] -= int(mal)


mipythmon = [[""],[""],[""]] # Espai per als pythmon del jugador		
# Avans de iniciar el joc et demana un nom
print "Quin es el tu nom?"
Nom = raw_input()

"""
(En estat de prova)D'un fitxer xml agafem les dades i comprovem si el nom que ha inreoduit
l'usuari hi es al fitxer xml i preguntar-li si vol continuar la partida
anterior 
"""
"""save = etree.parse('partida.xml')
jugadors = save.findall("jugador")
lj = len(jugadors)
for i in range(lj):
	if Nom == jugadors[i].attrib["nom"]:
		print "Tens una partida començada"
		p = jugadors[i].findall("pythmon")
		lp = len(p)
		for n in range(lp):
			mipythmon[n] = p[n].attrib["num"]
		c = jugadors[i].findall("combat")
		combat = c[0].attrib["cont"]
		joc(combat,mipythmon)
		break
	elif i == lj-1 and Nom != jugadors[lj-1].attrib["nom"]:
		print "Benvingut a la nostra torre Pythmon, guanya\na tots entrenadores i aconsegueix la vicotria"

if combat >= 10:
	exit()
"""

# Llista els pythmon en dos columnes per a que el jugador els pugui veure
for i in range(9):
	print str(i)+")",pythmon[i][0],"	",
	print str(9 + i) + ")",pythmon[9 + i][0]

# Demana al jugador que esculli 3 pythmon i els guarda
for i in range(3):
	escull = int(input("Escull el teu " + str(i + 1) + " pythmon: "))
	mipythmon[i] = pythmon[escull][:]

# Mostra els pythmon escollits pel jugador
for i in range(3):
		print mipythmon[i][0]


time.sleep(2.5)	
combat = 1


encombat=[[""],[""]]
contrari = [[""],[""],[""]] # Espai per als pythmon del oponent

while combat <= 10:
	clear()
	for i in range(3):
		rnd = random.randint(0,17)
		contrari[i] = pythmon[rnd][:]

	rotacio = 0
	encombat[0] = mipythmon[0]
	encombat[1] = contrari[rotacio]
	
	# Comença la animació del principi del combat
	pantalla(Nom + " el teu oponent sera en Marcos", 0)
	time.sleep(2)
	pantalla("Marcos a tret a " + encombat[1][0],1)
	time.sleep(1)
	pantalla("Has tret a " + encombat[0][0], 2)
	time.sleep(1)
	
	# Acaba la animacio d'inici del combat.
	while True:
		pantalla("Fes el teu moviment", 3)
		print "1)",encombat[0][6],"5) Pythmon"
		torn = int(input())
		if torn == 5:
			for i in range(3):
				print mipythmon[i][0]
			escull = int(input("Escull pythmon: "))
			encombat[0] = mipythmon[escull]
		elif torn > 0 and torn < 5:
			torn+= 5
			if encombat[0][torn] == "Llançaflames":
				Atac("Foc", 90,encombat,torn)
			elif encombat[0][torn] == "Surf":
				Atac("Aigua", 90,encombat,torn)
			elif encombat[0][torn] == "Gigadrenatge":
				Atac("Planta", 80,encombat,torn)
		time.sleep(1)
		if contrari[2][2] < 0:
			clear()
			print "\n\n\n\n\n\n\n"
			print "+-----------------------------------------------------------+"
			print " Has guanyat"
			print "+-----------------------------------------------------------+"
			time.sleep(2)
			break
		if encombat[1][2] < 1:
			rotacio += 1
			encombat[1] = contrari[rotacio]	
		clear()
	combat += 1
