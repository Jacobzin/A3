import math

print("Informe o tamanho do arquivo (MB)")
mb=float(input())
print("Qual a velocidade da internet (Mbps)")
vel=float(input())

calcs1=math.ceil(mb/vel)
calcm=math.ceil(calcs1//60)

print(f"O download ficará pronto em cerca de {calcm} minutos")