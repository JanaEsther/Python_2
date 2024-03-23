import math

lines = []

with open('data/vykaz.txt', encoding= 'utf-8') as file:
     for line in file:
       lines.append(int(line.strip()))
print(lines)

hodinova_mzda = int(input('Zadej hodinovou mzdu:'))
rocni_mzda = sum(lines) * hodinova_mzda
print(rocni_mzda)
prumer_mesic = math.ceil(rocni_mzda/12)
print(prumer_mesic)




            
