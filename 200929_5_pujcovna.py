"""
3
Půjčovna
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().
Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce, abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.
"""
import sys

"""
cesta = "200929_5_auta.txt"
soubor = open(cesta, encoding = "utf8")
"""
cesta = sys.argv[1]
soubor = open(cesta, encoding = "utf8")

radky = [radek for radek in soubor]
soubor.close()

print(radky)


"""print(radek[0].split(" ") for radek in radky]"""

cisla =  [radek.split(" ")[1].strip() for radek in radky if radek != '\n']  
""" for radek[0:-1] když chci odstranit jen poslední prázdný řádek"""

print(cisla)

"""cisla = [float(cislo) for cislo in cisla] - nebude fungovat, nejsou tam jen cisla, je třeba odstranit. des. čárky"""

cisla = [float(cislo.replace(",", ".")) for cislo in cisla] 

print(cisla)





