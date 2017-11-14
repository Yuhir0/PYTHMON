#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PYTHON  
# 
# Joc basat en Pokémon 
# Els monstres els anomenarem Pythmons
#
import random

print "Quin es el tu nom?"
Nom = raw_input()

print "Benvingut a la nostra torre Pythmon, guanya\na tots entrenadores i aconsegueix la vicotria"

def Surf():
	if enemic[1] == "Foc":
		mal = (90 + atacant[3] - enemic[4]) * 2
		print atacant[0],"ha usat Surf, es molt efectiu."
	elif enemic[1] == "Planta":
		mal = (90 + atacant[3] - enemic[4]) * 0.5
		print atacant[0],"ha usat Surf, no es gaire efetiu."
	else:
		mal = 90 + atacant[3] - enemic[4]
		print atacant[0],"ha usat Surf."
	enemic[2] -= int(mal)

def Llancaflames():
	if enemic[1] == "Planta":
		mal = (90 + atacant[3] - enemic[4]) * 2
		print atacant[0],"ha usat Llançaflames, es molt efectiu."
	elif enemic[1] == "Aigua":
		mal = (90 + atacant[3] - enemic[4]) * 0.5
		print atacant[0],"ha usat Llançaflames, no es gaire efectiu."
	else:
		mal = 90 + atacant[3] - enemic[4]
		print atacant[0],"ha usat Llançaflames."
	enemic[2] -= int(mal)

def Gigadrenatge():	
	if enemic[1] == "Aigua":
		mal = (80 + atacant[3] - enemic[4]) * 2
		print atacant[0],"ha usat Gigadrenatge, es molt efectiu."
	elif enemic[1] == "Foc":
		mal = (80 + atacant[3] - enemic[4]) * 0.5
		print atacant[0],"ha usat Gigadrenatge, no es gaire efectiu."
	else:
		mal = 80 + atacant[3] - enemic[4]
		print atacant[0],"ha usat Gigadrenatge."
	enemic[2] -= int(mal)

contrari = [[""],[""],[""]]
mipythmon = [[""],[""],[""]]
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
for i in range(3):
	rnd = random.randint(0,17)
	contrari[i] = pythmon[rnd]

for i in range(9):
	print str(i)+")",pythmon[i][0],"	",
	print str(9 + i) + ")",pythmon[9 + i][0]

for i in range(3):
	escull = int(input("Escuell el teu " + str(i + 1) + " pythmon: "))
	mipythmon[i] = pythmon[escull]
	
for i in range(3):
	print mipythmon[i][0]

atacant = mipythmon[0]
enemic = contrari[0]
while mipythmon[0][2] > 0 and mipythmon[1][2] > 0 and mipythmon[2][2] > 0 or contrari[0][2] > 0 and contrari[1][2] > 0 and contrari[2][2] >0:
	print enemic[0],"|vida:",enemic[2]
	print ""
	print ""
	print ""
	print atacant[0],"|vida:",atacant[2]
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
		elif atacant[torn+5] == "Surf":
			Surf()
		elif atacant[torn+5] == "Gigadrenatge":
			Gigadrenatge()
