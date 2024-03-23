
vykaz = []

with open('data/vykaz.txt', encoding ='utf-8') as file:
    for line in file:
        vykaz.append(line.strip())

print(vykaz)

hodinova_mzda = int(input("Zadej hodinovou mzdu:"))
mesicni_mzdy = []
with open('data/vykaz.txt', encoding ='utf-8') as file:
    for line in file:
        mesic = int(line.strip())
        mesicni_mzda =mesic * hodinova_mzda
        mesicni_mzdy.append(mesicni_mzda)
        print(mesicni_mzda)

with open ('mesicni_mzda.txt', mode="w", encoding='utf-8') as output_file:
    for mzda in mesicni_mzdy:
        print(mzda, file=output_file)