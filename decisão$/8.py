a=float(input("Digite o valor do primeiro produto: "))
b=float(input("Digite o valor do segundo produto: "))
c=float(input("Digite o valor do terceiro produto: "))

if a<b and a<c:
    print("Compre o primeiro produto")
elif b<a and b<c:
    print("Compre o segundo produto")
elif c<a and c<b:
    print("Compre o terceiro produto")