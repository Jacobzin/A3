turno=str(input("Informe seu turno (M-matutino ou V-Vespertino ou N- Noturno) "))
if turno==("M"):
    print("Bom dia!")
elif turno==("V"):
    print("Boa tarde!")
elif turno==("N"):
    print("Boa noite!")
else:
    print("Turno invalido!")