primeiro=float(input("Escreva o primeiro numero: "))
segundo=float(input("Escreva o segundo numero: "))
if primeiro>segundo:
    print(f"O numero {primeiro:.1f} é maior que {segundo:.1f}")
elif segundo>primeiro:
    print(f"O numero {segundo:.2f} é maior que {primeiro:.1f}")
elif primeiro>=segundo:
    print(f"Os numeros são iguais")