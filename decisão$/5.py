
nota=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))

media=(nota+nota2)/2

if media==10:
    print("Aprovado com Distinção")
elif media>=7:
    print("Aprovado")
elif media<=7:
    print("Reprovado")