import math

print("Insira o peso dos peixes")
peso=float(input())
if peso>50:
    ex=math.ceil(peso-50)
    print("Você exedeu %s" %(ex))
    multa=math.ceil(ex*4)
    print("E pagará R$%s" %(multa))
else:
    print("Parabens você não pagará multa")