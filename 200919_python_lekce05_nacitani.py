soubor = open(r"C:\Users\Martina\Documents\Digitální akademie_PP2020\Python\200923_mereni.txt", encoding = "utf8")  #je nutné mít ve stejné složce, nebo vypsat celou cestu
#"c:/Users/Martina/Documents/Digitální akademie_PP2020/Python/"
radky = [radek for radek in soubor]
soubor.close()

print(radky)

#fungovalo by replace???
ciste_radky = [udaj.strip() for udaj in radky]
print(ciste_radky)


# udělá seznam seznamů, se dvěma prvky [['po', '17.3'], ['út', '16.8'], ['st', '15.1'], ['čt', '13.2'], ['pá', '14.0'], ['so', '13.9'], ['ne', '15.8']]
split = [udaj.split("\t") for udaj in ciste_radky]
print(split)


dny_v_tydnu = [udaj.split("\t")[0] for udaj in ciste_radky]
teploty = [float(udaj.split("\t")[1]) for udaj in ciste_radky]
print(dny_v_tydnu)
print(teploty)

prumerna_teplota = sum(teploty) / len(teploty)
print(round(prumerna_teplota,2))
print(prumerna_teplota)

# udělá seznam seznamů, se dvěma prvky [['po', '17.3'], ['út', '16.8'], ['st', '15.1'], ['čt', '13.2'], ['pá', '14.0'], ['so', '13.9'], ['ne', '15.8']]
split = [udaj.split("\t") for udaj in ciste_radky]
print(split)
