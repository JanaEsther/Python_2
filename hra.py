print ("Vešel jsi do chrámu a vytoužená koruna leží na podstavci. Rozběhneš se za ní? [A/N]!")
volba = input()

if (volba == "a"):
  print("Podivný zvuk pod tvými podrážkami zasignoval, že něco není v pořádku.")
  print("Stiskl jsi past a stěny se začaly posouvat k tobě, východ se zavírá. KONEC HRY")
else:
  print("Všiml sis tlačítka v podlaze, které jsi opatrně obešel. Stojíš přímo před korunou.")
  print("Sebereš ji? [A/N]")
volba2= input()
if (volba2 == "a"):
  print("Vítězoslavně jsi vyzdvihl korunu! Ale všiml sis, že není to jediné, co máš v ruce.")
  print("Po rukávu ti putuje obří tarantula, něco tě zabolelo a padl jsi.KONEC HRY")
else:
  print("Rozvážnost se ti znova vyplatila, z pod koruny něbo vylezlo a ztratilo sea v temnotě")
  print(" Korunu jsi sebral a rychle utekl ven ba boží světlo. VYHRÁL JSI!.")

