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

# Es l'apariencia de cada moment del joc (animacions)
def pantalla(text,escena):
	encombat0 = ""
	encombat1 = ""

	# Les dades dels pythmon que es mostraran, en cas de tenir efectes
	if encombat[0][0] != "":
		if encombat[0][10] != "N" and encombat[0][11] != "N":
			encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " | [" + encombat[0][10] + "] [" + encombat[0][11] + "]"
		elif encombat[0][10] != "N":
			encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " | [" + encombat[0][10] + "]"
		elif encombat[0][11] != "N":
			encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " | [" + encombat[0][11] + "]"
		else:
			encombat0 = "| " + encombat[0][0] + ": " + str(encombat[0][2]) + " |"

		if encombat[1][10] != "N" and encombat[1][11] != "N":
			encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " | [" + encombat[1][10] + "] [" + encombat[1][11] + "]"
		elif encombat[1][10] != "N":
			encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " | [" + encombat[1][10] + "]"
		elif encombat[1][11] != "N":
			encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " | [" + encombat[1][11] + "]"
		else:
			encombat1 = "| " + encombat[1][0] + ": " + str(encombat[1][2]) + " |"
			
	escriu = " "

	# Encara no hi ha combat, per tant hi ha una pantalla en negre i només es fa l'animació del text
	if escena == 0:
		for i in text:
			escriu += i
			print "\n\n\n\n\n\n\n"
			print "+-----------------------------------------------------+"
			print escriu
			print "+-----------------------------------------------------+"
			time.sleep(0.03)
			clear()
		print "\n\n\n\n\n\n\n"
		print "+-----------------------------------------------------+"
		print escriu
		print "+-----------------------------------------------------+"

	# L'enemic treu un pythmon, animació de text + sortida al camp del pythmon
	elif escena == 1:
		for i in text:
			escriu += i
			clear()
			print "\n\n\n\n\n\n\n"
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
			print "\n\n\n\n\n\n"
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
			print "\n\n\n\n\n\n"
			print "+-----------------------------------------------------+"
			print escriu
			print "+-----------------------------------------------------+"
			time.sleep(0.03)
		
		time.sleep(0.3)
		
		# Animació de quan el jugador treun un Pythmon
		for i in range(5,-1,-1):
			clear()
			print "\t\t\t\t" + encombat1
			print "\n\n\n\n\n"
			for j in range(i,0,-1):
				print "\t",
			print encombat0
			print "+-----------------------------------------------------+"
			print escriu
			print "+-----------------------------------------------------+"
			time.sleep(0.2)

	# Els dos pythmon estan en combat, només es fa l'animació del text
	elif escena == 3:
		for i in text:
			escriu += i
			clear()
			print "\t\t\t\t" + encombat1
			print "\n\n\n\n\n"
			print encombat0
			print "+-----------------------------------------------------+"
			print escriu
			print "+-----------------------------------------------------+"
			time.sleep(0.03)


# Es defineixen els atacs
def Atac(tipus,potencia,atacant,defensor,torn,efecte):
	
	if potencia != 0:
		# Atacs molt efectius
		if tipus == "Planta" and defensor[1] == "Aigua" or tipus == "Foc" and defensor[1] == "Planta" or tipus == "Aigua" and defensor[1] == "Foc":
			mal = (potencia + atacant[3] - defensor[4]) * 2
			pantalla(atacant[0] + " ha usat " + atacant[torn] + ", es molt efectiu.", 3)
		
		# Atacs poc efectius
		elif tipus == "Planta" and defensor[1] == "Foc" or tipus == "Foc" and defensor[1] == "Aigua" or tipus == "Aigua" and defensor[1] == "Planta":
			mal = (potencia + atacant[3] - defensor[4]) * 0.5
			pantalla(atacant[0] + " ha usat " + atacant[torn] + ", no es gaire efectiu.", 3)
			
		# Atacs efectius
		else:
			mal = potencia + atacant[3] - defensor[4]
			pantalla(atacant[0] + " ha usat " + atacant[torn] + ".", 3)
		
		# Si l'atac entra en el 5% farà el doble de mal (crític)
		if random.randint(1,100) <= 5: 
			defensor[2] -= int(mal) * 2
		else:
			defensor[2] -= int(mal)
		
	probabilitat = random.randint(1,100)
	
	# Efectes d'estat
	# Si el pythmon no és de foc, i no té cap efecte d'estat, es pot cremar.
	if efecte[0] == "C" and defensor[10] == "N" and defensor[1] != "Foc": 
		if efecte[1].isdigit():
			if probabilitat <= int(efecte[1:]):
				defensor[10] = "C"
		else:
			if probabilitat <= int(efecte[2:]):
				defensor[10] = "C"
				
	# Si el pythmon no té cap efecte d'estat, es pot paralitzar.
	elif efecte[0] == "P" and defensor[10] == "N":
		if probabilitat <= int(efecte[1:]):
			defensor[10] = "P"
			
	# Si el pythmon no té cap efecte d'estat, es pot dormir.
	elif efecte[0] == "S" and defensor[10] == "N":
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
	elif efecte[0] == "D":
		defensor[11] == "D"
		
	# Drenatge
	elif efecte[0] == "G":
		atacant[2] += int(int(efecte[1:]) * mal / 100)
	
	return "N" # En cas de que no hi hagi retrocés
	
""" 
Aqui estan tos els pythmon amb el seguient ordre Nom, Tipus, Vida, Atac, Defensa,
Velocitat, Atac1, Atac2, Atac3.
"""
pythmon = [["Bulbasaur","Planta",231,147,134,126,"Fulla_Afilada","Gigadrenatge","Placatge","Drenadores","N","N"],
		["Ivysaur","Planta",261,176,162,156,"Fulla_Afilada","Gigadrenatge","Drenadores","Placatge","N","N"],
		["Venusaur","Planta",301,220,202,196,"Gigadrenatge","Raig_Solar","Esporas","Dansa_Espasa","N","N"],
		["Squirtle","Aigua",229,145,166,122,"Surf","Atac Rapid","Acua_Jet","Placatge","N","N"],
		["Wartortle","Aigua",259,178,196,152,"Surf","Acua_Jet","Cop_Cos","Cascada","N","N"],
		["Blastoise","Aigua",299,222,236,192,"Surf","Hidrobomba","Cop_Cos","Dansa_Espasa","N","N"],
		["Charmander","Foc",219,154,122,166,"Llançaflames","Atac_Rapid","Ullal_Igni","Placatge","N","N"],
		["Charmeleon","Foc",257,180,152,196,"Llançaflames","Ullal_Igni","Placatge","Dansa_Espasa","N","N"],
		["Charizard","Foc",297,224,192,236,"Llançaflames","Flamarada","Hiper_Raig","Dansa Espasa","N","N"],
		["Vulpix","Foc",217,129,116,166,"Llançaflames","Ullal Igni","Foc_Fatuo","Atac_Rapid","N","N"],
		["Ninetales","Foc",287,206,186,236,"Llançaflames","Foc_Fatuo","Flamarada","Atac_Rapid","N","N"],
		["Exeggcute","Planta",261,127,196,116,"Fulla_Afilada","Gigadrenatge","Esporas","Placatge","N","N"],
		["Exeggutor","Planta",331,248,206,146,"Gigadrenatge","Esporas","Raig_Solar","Hiper_Raig","N","N"],
		["Staryu","Aigua",201,138,146,206,"Surf","Atac_Rapid","Acua_Jet","Cascada","N","N"],
		["Starmie","Aigua",261,204,206,266,"Surf","Atac_Rapid","Hidrobomba","Acua_Jet","N","N"],
		["Magmar","Foc",271,248,150,222,"Llançaflames","Hiper_Raig","Foc_Fatuo","Flamarada","N","N"],
		["Tangela","Planta",271,160,266,156,"Gigadrenatge","Esporas","Drenadores","Raig_Solar","N","N"],
		["Lapras","Aigua",401,226,196,156,"Surf","Cop_Cos","Hidrobomba","Cascada","N","N"],
		["Magikarp","Aigua",999,999,999,1,"Perforador","Esquitxada","Esquitxada","Perforador","N","N"]]

mipythmon = [[""],[""],[""]] # Espai per als pythmon del jugador		
encombat=[[""],[""]]

# Abans d'iniciar el joc et demana un nom
pantalla("Quin es el tu nom?",0)
Nom = raw_input()

combat = 1 # Identifica la ronda per la que va el jugador

"""
(En estat de prova)D'un fitxer xml agafem les dades i comprovem si el nom que ha inreoduit
l'usuari hi es al fitxer xml i preguntar-li si vol continuar la partida
anterior 
"""

partida = etree.parse('partida.xml') # Carreguem el fixer 'partida.xml' que conté les dades dels jugadors
jugadors = partida.findall("jugador") # Trobem tots el jugadors

lj = len(jugadors) # Averigüem quants jugadors són

for i in range(lj):
	if Nom == jugadors[i].attrib["nom"]:
		num = i # Guardara la pocicio del jugador a la llista
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
		print str(i)+")",pythmon[i][0],"	",
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
	num = len(jugadors) - 1

# Guardem totes les dades formulades del xml al fitxer 'partida.xml'			
partida.write('partida.xml')

time.sleep(2.5)	

contrari = [[""],[""],[""]] # Espai per als pythmon del oponent

# Aquí tenim la llista amb els noms dels entrenadors rivals
entrenadors = ["Marcos","Ana","Marta","Tarazona","teu oponent","Joan","David","Paula","Carles","Sergi","Pablo","Wenceslau","Nacho","Amelia","Joaquim","Arantxa","Alvaro"]

# Aquí es desenvolupa la major part del joc.
while combat <= 10:
	clear()
	
	# S'escullen els Pythmon del contrari
	for i in range(3):
		rnd = random.randint(0,17)
		contrari[i] = pythmon[rnd][:]
	
	rotacio = 0
	encombat[0] = mipythmon[0]
	encombat[1] = contrari[rotacio] # Cada cop que es mori un pythmon el contrari canviara al següent
		
	joy = mipythmon[:] # Faig que la variable joy tingui les dades dels pythmon del jugador per més endevant
	
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
		print "1) " + encombat[0][6] + "\t2) " + encombat[0][7] + "\t5) Pythmon"
		print "3) " + encombat[0][8] + "\t4) " + encombat[0][9]
		juga = int(input())
		if juga == 5:
			pantalla("Escull pythmon: ", 3)
			for i in range(3):
				print str(i+1) + ") " + mipythmon[i][0]
			escull = int(input())
			
			# Controla que la informació introduida sigui correcte i no pugui canviar a un pythmon que esta devilitat
			while escull < 1 or escull > 3 or mipythmon[escull - 1][2] < 1:
				pantalla("Siusplau, introdueix un numero correcte: ", 3)
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
			
			# Els Atacs
			if encombat[fst][10] == "P" and random.randint(0,2) == 0:
				pantalla(encombat[fst][0] + " està paralitzat, no pot atacar!", 3)
		#	elif encombat[fst][10] == "S" and random.randint(0,2) == 0:
		#		pantalla(encombat[fst][0] + " està dormit, no pot atacar!", 3)
		#		if random.randint(0,3) == 0:
		#			encombat[fst][10] == "N"
		#			pantalla(encombat[fst][0] + " s'ha despertat!", 3)
		#	elif encombat[fst][10] == "C":
		#		encombat[fst][2] - 25
		#		pantalla(encombat[fst][0] + " està cremat! ", 3)
			else:
				retroces = ""
				if encombat[fst][torn + 5] == "Llançaflames":
					retroces = Atac("Foc", 90,encombat[fst],encombat[snd],torn + 5,"C10")
				elif encombat[fst][torn + 5] == "Flamarada":
					retroces = Atac("Foc", 120,encombat[fst],encombat[snd],torn + 5,"C30")
				elif encombat[fst][torn + 5] == "Ullal_Igni":
					retroces = Atac("Foc", 65,encombat[fst],encombat[snd],torn + 5,"CR10")
				elif encombat[fst][torn + 5] == "Foc_Fatuo":
					retroces = Atac("Foc", 0,encombat[fst],encombat[snd],torn + 5,"C100")
				elif encombat[fst][torn + 5] == "Surf":
					retroces = Atac("Aigua", 90,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Hidrobomba":
					retroces = Atac("Aigua", 110,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Acua_Jet":
					retroces = Atac("Aigua", 40,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Cascada":
					retroces = Atac("Aigua", 80,encombat[fst],encombat[snd],torn + 5,"R30")
				elif encombat[fst][torn + 5] == "Gigadrenatge":
					retroces = Atac("Planta", 80,encombat[fst],encombat[snd],torn + 5,"G30")
				elif encombat[fst][torn + 5] == "Fulla_Afilada":
					retroces = Atac("Planta", 55,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Raig_Solar":
					retroces = Atac("Planta", 120,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Esporas":
					retroces = Atac("Planta", 0,encombat[fst],encombat[snd],torn + 5,"S100")
				elif encombat[fst][torn + 5] == "Drenadores":
					retroces = Atac("Planta", 0,encombat[fst],encombat[snd],torn + 5,"D")
				elif encombat[fst][torn + 5] == "Placatge":
					retroces = Atac("Normal",40,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Atac_Rapid":
					retroces = Atac("Normal",40,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Cop_Cos":
					retroces = Atac("Normal",85,encombat[fst],encombat[snd],torn + 5,"P30")
				elif encombat[fst][torn + 5] == "Dansa_Espasa":
					retroces = Atac("Normal",0,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Perforador":
					retroces = Atac("Normal",9999,encombat[fst],encombat[snd],torn + 5,"N")
				elif encombat[fst][torn + 5] == "Hiper_Raig":
					retroces = Atac("Normal",150,encombat[fst],encombat[snd],torn + 5,"N")
					
				# Quan es devilita el pythmon, s'acaba la ronda d'atacs
				if encombat[0][2] < 1:
					encombat[0][2] = 0
					pantalla(encombat[0][0] + " s'ha devilitat",3)
					time.sleep(0.5)
					cops = 2
				if encombat[1][2] < 1:
					encombat[1][2] = 0
					pantalla(encombat[1][0] + " s'ha devilitat",3)
					time.sleep(0.5)
					cops = 2
					
				time.sleep(1)
					
				# Si un dels pythmon retrocedeix
				if retroces == "R" and cops == 0 and encombat[snd][2] > 0: # Si retroces es igual a 'R' vol dir que el pythmon retrocedira
					pantalla(encombat[snd][0] + " ha retrocedit", 3)
					cops = 2
			time.sleep(1)
				
			cops += 1
		time.sleep(1)
		
		# Si es devilita tot l'equip del contrari
		if contrari[2][2] < 1:
			encombat[1][2] = 0
			pantalla(encombat[1][0] + " s'ha devilitat",3)
			time.sleep(1)
			pantalla("Has guanyat el combat",0)
			time.sleep(2)
			break
			
		# Si es devilita un pythmon del contrari
		elif encombat[1][2] < 1:
			encombat[1][2] = 0
			pantalla(encombat[1][0] + " s'ha devilitat",3)
			rotacio += 1
			encombat[1] = contrari[rotacio]
			time.sleep(0.5)
			pantalla(entrenadors[entrenador] + " a tret a " + encombat[1][0],1)
		
		# Si es devilita tot l'equip del jugador
		if mipythmon[0][2] < 1 and mipythmon[1][2] < 1 and mipythmon[2][2] < 1:
			pantalla("Has perdut",0)
			combat = 10
			break
			
		# Si es devilita un pythmon del jugador
		elif encombat[0][2] < 1:
			pantalla("Escull pythmon: ", 3)
			for i in range(3):
				print str(i+1) + ") " + mipythmon[i][0]
			escull = int(input())
			
			# Controla que la informació introduida sigui correcte i no pugui canviar a un pythmon que esta devilitat
			while escull < 1 or escull > 3 or mipythmon[escull - 1][2] < 1:
				pantalla("Siusplau, introdueix un numero correcte: ", 3)
				for i in range(3):
					print str(i+1) + ") " + mipythmon[i][0]
				escull = int(input())
			encombat[0] = mipythmon[escull - 1]
		clear()
	mipythmon = joy[:] # Amb això faig que les estadístiques dels pythmon de l'usuari tornin a l'estat original
	combat += 1
	
	jugadors[num].find("combat").attrib["cont"]=str(combat)
	
	# Guardem totes les dades formulades del xml al fitxer 'partida.xml'			
	partida.write('partida.xml')
