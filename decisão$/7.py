prim=(input("Digite o primeiro numero: "))
sec=(input("Digite o segundo numero: "))
terc=(input("Digite o terceiro numero: "))

if prim>sec and prim>terc:
    print(f"O nuemero {prim} é o maior.")
elif sec>prim and sec>terc:
    print(f"O numero {sec} é o maior")
elif terc>prim and terc>sec:
    print(f"O numero {terc} é o maior")
if prim<sec and prim<terc:
    print(f"O nuemero {prim} é o menor.")
elif sec<prim and sec<terc:
    print(f"O numero {sec} é o menor")
elif terc<prim and terc<sec:
    print(f"O numero {terc} é o menor")