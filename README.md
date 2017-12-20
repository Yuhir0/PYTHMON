# PYTHMON

## Diseny

Bassant-nos en la famosa saga de jocs POKEMON em realitzat la nostra versió anomenada PYTHMON (Python Monsters).

Ens em bassat en les característiques de les diferents generacions de Pokémon, però principalment en les de la primera generació

Els Pythmon només tenen un tipus: Foc, Planta o Aigua.
Hi ha atacs dels tres tipus i de tipus normal.
Em fet que els tipus tinguin la següent relació Foc > Planta > Aigua > Foc.
Si es molt efectiu el mal augmenta x2, si es poc efectiu el mal disminueix x0.5, si es normal (ex. Foc vs Foc)
El jugador començarà escollint 3 Pythmon per jugar.
A la pantalla es mostra el Pythmon enemic i el Pythmon del jugador amb la seva vida i el seu estat (Pot estar dormit, cremat, paralitzat o amb drenadores).
Les opcions que té el jugador en el combat son els 4 atacs i l'opció de canviar de Pythmon, si el jugador canvia de Pythmon el Pythmon rival atacarà al Pythmon que treu el jugador.
Si el jugador guanya als 10 entrenadors, passarà a ser el campió i serà l'últim entrenador rival (amb els Pythmon que hagi escollit per guanyar) per als pròxims jugadors.
## Opcions per al normal funcionament

Per a poder jugar a aquest joc requereix:
- Tenir instal·lada la llibreria **python-lxml** per a la versio 2.7 de python
    - (Windows) Per instal·lar la llibreria python-lxml pots usar els instal·ladors del directori Recursos
    - (Linux - based on Debian) Per instal·lar la llibreria python-lxml pots usar la comanda "apt install python-lxml"
    - En cas d'altres sistemes pots anar a la pagina oficial [Enllaç](https://pypi.python.org/pypi/lxml/3.4.0)
- Executar el programa Pythmon.py desdel seu propi directori, i el directori a de contenir el nom "PYTHMON"

