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





# Es defineixen els atacs
def Surf():
	if enemic[1] == "Foc":
		mal = (90 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Surf, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Planta":
		mal = (90 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Surf, no es gaire efetiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 90 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Surf."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)
	
def Hidrobomba():
	if enemic[1] == "Foc":
		mal = (110 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Hidrobomba, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Planta":
		mal = (110 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Hidrobomba, no es gaire efetiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 110 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Hidrobomba."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)
	
def Pistoladaigua():
	if enemic[1] == "Foc":
		mal = (40 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Pistola d'aigua, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Planta":
		mal = (40 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Pistola d'aigua, no es gaire efetiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 40 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Pistola d'aigua."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)

def Cascada():
	if enemic[1] == "Foc":
		mal = (80 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Cascada, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Planta":
		mal = (80 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Cascada, no es gaire efetiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 80 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Cascada."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)

def Acuajet():
	if enemic[1] == "Foc":
		mal = (40 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Acua jet, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Planta":
		mal = (40 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Acua jet, no es gaire efetiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 40 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Acua jet."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)
# Hay que hacer que acua jet ataque antes

def Copcos():
	mal = 85 + atacant[3] - enemic[4]
	clear()
	escenari()
	print "+-----------------------------------------------------------+"
	print atacant[0],"ha usat Cop cos."
	print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)
	
def Esquitxada():
	mal = 0 * atacant[3]
	clear()
	escenari()
	print "+-----------------------------------------------------------+"
	print atacant[0],"ha usat Esquitxada... És inútil."
	print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)

def Hiperraig():
	mal = 85 + atacant[3] - enemic[4]
	clear()
	escenari()
	print "+-----------------------------------------------------------+"
	print atacant[0],"ha usat Hiper Raig."
	print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)
	clear()
	escenari()
	print "+-----------------------------------------------------------+"
	print atacant[0],"està descansant."
	print "+-----------------------------------------------------------+"
# Hay que hacer que el pokemon descanse un turno

def Dansaespasa():
#	mal = (atacant[3] * 2)
	clear()
	escenari()
	print "+-----------------------------------------------------------+"
	print atacant[0],"ha usat Dansa espasa. El seu atac ha pujat!"
	print "+-----------------------------------------------------------+"
#	atacant[3] = atacant[3]*2
# No sé si está bien xd
def Llancaflames():
	if enemic[1] == "Planta":
		mal = (90 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Llançaflames, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Aigua":
		mal = (90 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Llançaflames, no es gaire efectiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 90 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Llançaflames."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)
def Flamarada():
	if enemic[1] == "Planta":
		mal = (120 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Flamarada, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Aigua":
		mal = (120 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Flamarada, no es gaire efectiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 120 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Flamarada."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)

def Ullaligni():
	if enemic[1] == "Planta":
		mal = (65 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Ullal Igni, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Aigua":
		mal = (65 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Ullal Igni, no es gaire efectiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 65 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Ullal Igni."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)

def Gigadrenatge():	
	if enemic[1] == "Aigua":
		mal = (80 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Gigadrenatge, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Foc":
		mal = (80 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Gigadrenatge, no es gaire efectiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 80 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Gigadrenatge."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)

def Raigsolar():	
	if enemic[1] == "Aigua":
		mal = (120 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Raig Solar, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Foc":
		mal = (120 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Raig Solar, no es gaire efectiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 120 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Raig Solar."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)
# Hay que hacer que rayo solar tarde un turno en ejecutarse

def Fullafilada():	
	if enemic[1] == "Aigua":
		mal = (55 + atacant[3] - enemic[4]) * 2
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Fulla Afilada, es molt efectiu."
		print "+-----------------------------------------------------------+"
	elif enemic[1] == "Foc":
		mal = (55 + atacant[3] - enemic[4]) * 0.5
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Fulla Afilada, no es gaire efectiu."
		print "+-----------------------------------------------------------+"
	else:
		mal = 55 + atacant[3] - enemic[4]
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print atacant[0],"ha usat Fulla Afilada."
		print "+-----------------------------------------------------------+"
	enemic[2] -= int(mal)

# Es l'apariencia del escenari.
def escenari():
	print "			",enemic[0],"|vida:",enemic[2]
	print "\n\n\n\n"
	print atacant[0],"|vida:",atacant[2]

contrari = [[""],[""],[""]] # Espai per als pythmon del oponent
mipythmon = [[""],[""],[""]] # Espai per als pythmon del jugador

""" 
Aqui estan tos els pythmon amb el seguient ordre Nom, Tipus, Vida, Atac, Defensa,
Velocitat, Atac1, Atac2, Atac3.
"""
pythmon = [["Bulbasaur","Planta",231,147,134,126],
		["Ivysaur","Planta",261,176,162,156],
		["Venusaur","Planta",301,220,202,196,"Gigadrenatge","Raigsolar","Copcos"],
		["Squirtle","Aigua",229,145,166,122],
		["Wartortle","Aigua",259,178,196,152],
		["Blastoise","Aigua",299,222,236,192,"Surf","Copcos","Hidrobomba"],
		["Charmander","Foc",219,154,122,166],
		["Charmeleon","Foc",257,180,152,196,],
		["Charizard","Foc",297,224,192,236,"Llançaflames","Hiperraig","Flamarada"],
		["Vulpix","Foc",217,129,116,166],
		["Ninetales","Foc",287,206,186,236,"Ullaligni","Flamarada","Dansaespasa"],
		["Exeggcute","Planta",261,127,196,116],
		["Exeggutor","Planta",331,248,206,146,"Fullaafilada","Raigsolar","Copcos"],
		["Staryu","Aigua",201,138,146,206],
		["Starmie","Aigua",261,204,206,266,"Acuajet","Hidrobomba","Surf"],
		["Magmar","Foc",271,248,150,222],
		["Tangela","Planta",271,160,266,156],
		["Lapras","Aigua",401,226,196,156,"Cascada","Copcos","Hidrobomba"],
		["Magikarp","Aigua",999,999,999,1,"Esquitxada"]]

# S'executa el joc
def joc(combat):
	while combat <= 10:
		print combat
		for i in range(3):
			rnd = random.randint(0,17)
			contrari[i] = pythmon[rnd]
		rotacio = 0
		atacant = mipythmon[0]
		enemic = contrari[rotacio]
		
		# Comença la animació del principi del combat
		print "\n\n\n\n\n\n\n"
		print "+-----------------------------------------------------------+"
		print "",Nom, "el teu oponent sera en Marcos"
		print "+-----------------------------------------------------------+"
		time.sleep(2)
		clear()
		print enemic[0],"|vida:",enemic[2]
		print "\n\n\n\n\n\n"
		print "+-----------------------------------------------------------+"
		print " Marcos a tret a", enemic[0]
		print "+-----------------------------------------------------------+"
		time.sleep(0.3)
		clear()
		print "	",enemic[0],"|vida:",enemic[2]
		print "\n\n\n\n\n\n"
		print "+-----------------------------------------------------------+"
		print " Marcos a tret a", enemic[0]
		print "+-----------------------------------------------------------+"
		time.sleep(0.3)
		clear()
		print "		",enemic[0],"|vida:",enemic[2]
		print "\n\n\n\n\n\n"
		print "+-----------------------------------------------------------+"
		print " Marcos a tret a", enemic[0]
		print "+-----------------------------------------------------------+"
		time.sleep(0.3)
		clear()
		print "			",enemic[0],"|vida:",enemic[2]
		print "\n\n\n\n\n\n"
		print "+-----------------------------------------------------------+"
		print " Marcos a tret a", enemic[0]
		print "+-----------------------------------------------------------+"
		time.sleep(1)
		clear()
		print "			",enemic[0],"|vida:",enemic[2]
		print "\n\n\n\n\n"
		print "			",atacant[0],"|vida:",atacant[2]
		print "+-----------------------------------------------------------+"
		print " Has tret a", atacant[0]
		print "+-----------------------------------------------------------+"
		time.sleep(0.3)
		clear()
		print "			",enemic[0],"|vida:",enemic[2]
		print "\n\n\n\n\n"
		print "		",atacant[0],"|vida:",atacant[2]
		print "+-----------------------------------------------------------+"
		print " Has tret a", atacant[0]
		print "+-----------------------------------------------------------+"
		time.sleep(0.3)
		clear()
		print "			",enemic[0],"|vida:",enemic[2]
		print "\n\n\n\n\n"
		print "	",atacant[0],"|vida:",atacant[2]
		print "+-----------------------------------------------------------+"
		print " Has tret a", atacant[0]
		print "+-----------------------------------------------------------+"
		time.sleep(0.3)
		clear()
		escenari()
		print "+-----------------------------------------------------------+"
		print " Has tret a", atacant[0]
		print "+-----------------------------------------------------------+"
		# Acaba la animacio d'inici del combat.
		
		clear()
		escenari()
		while True:
			print "+-----------------------------------------------------------+"
			print " Fes el teu moviment"
			print "+-----------------------------------------------------------+"
			print "1)",atacant[6],"5) Pythmon"
			torn = int(input())
			if torn == 5:
				for i in range(3):
					print mipythmon[i][0]
				escull = int(input("Escull pythmon: "))
				atacant = mipythmon[escull]
			elif torn > 0 and torn < 5:
				if atacant[torn+5] == "Llançaflames":
					Llancaflames()
				elif atacant[torn+5] == "Flamarada":
					Flamarada()
				elif atacant[torn+5] == "Ullaligni":
					Ullaligni()
				elif atacant[torn+5] == "Hiperraig":
					Hiperraig()
				elif atacant[torn+5] == "Hidrobomba":
					Hidrobomba()
				elif atacant[torn+5] == "Cascada":
					Cascada()
				elif atacant[torn+5] == "Acuajet":
					Acuajet()
				elif atacant[torn+5] == "Copcos":
					Copcos()
				elif atacant[torn+5] == "Gigadrenatge":
					Gigadrenatge()
				elif atacant[torn+5] == "Raigsolar":
					Raigsolar()
				elif atacant[torn+5] == "Fullaafilada":
					Fullaafilada()
				elif atacant[torn+5] == "Esquitxada":
					Esquitxada()
				elif atacant[torn+5] == "Dansaespasa":
					Dansaespasa()
			time.sleep(1)
			if contrari[2][2] < 0:
				clear()
				print "\n\n\n\n\n\n\n"
				print "+-----------------------------------------------------------+"
				print " Has guanyat"
				print "+-----------------------------------------------------------+"
				time.sleep(2)
				break
			if enemic[2] < 1:
				rotacio += 1
				enemic = contrari[rotacio]	
			clear()
			escenari()
		combat += 1
		
# Avans de iniciar el joc et demana un nom
print "Quin es el tu nom?"
Nom = raw_input()

"""
(En estat de prova)D'un fitxer xml agafem les dades i comprovem si el nom que ha inreoduit
l'usuari hi es al fitxer xml i preguntar-li si vol continuar la partida
anterior 
"""
save = etree.parse('partida.xml')
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
		joc(combat)
		break
	elif i == j-1 and Nom != jugadors[j-1].attrib["nom"]:
		print "Benvingut a la nostra torre Pythmon, guanya\na tots entrenadores i aconsegueix la vicotria"

if combat >= 10:
	exit()
	
# Llista els pythmon en dos columnes per a que el jugador els pugui veure
for i in range(9):
	print str(i)+")",pythmon[i][0],"	",
	print str(9 + i) + ")",pythmon[9 + i][0]

# Demana al jugador que esculli 3 pythmon i els guarda
for i in range(3):
	escull = int(input("Escuell el teu " + str(i + 1) + " pythmon: "))
	mipythmon[i] = pythmon[escull]

# Mostra els pythmon escollits pel jugador
for i in range(3):
		print mipythmon[i][0]

time.sleep(5)	
clear() 
combat = 1
joc(combat)
