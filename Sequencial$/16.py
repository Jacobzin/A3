import math

area = float(input("Informe a área a ser pintada em metros quadrados: "))
litros_necessarios = math.ceil(area / 3) 
preco_lata = 80.00
litros_por_lata = 18
preco_galao = 25.00
litros_por_galao = 3.6

latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)
galoes_necessarios = math.ceil(litros_necessarios / litros_por_galao)
preco_total_latas = latas_necessarias * preco_lata
preco_total_galoes = galoes_necessarios * preco_galao
latas_compradas = litros_necessarios // litros_por_lata
litros_restantes = litros_necessarios % litros_por_lata
galoes_comprados = math.ceil(litros_restantes / litros_por_galao)
preco_total_combinado = (latas_compradas * preco_lata) + (galoes_comprados * preco_galao)

print(f"Você precisará de {litros_necessarios:.2f} litros de tinta.")
print(f"Opção 1: Compre apenas latas de 18 litros - você precisará de {latas_necessarias} latas e pagará R${preco_total_latas:.2f}.")
print(f"Opção 2: Compre apenas galões de 3,6 litros - você precisará de {galoes_necessarios} galões e pagará R${preco_total_galoes:.2f}.")
print(f"Opção 3: Compre a combinação mais barata de latas e galões - você precisará de {latas_compradas} latas e {galoes_comprados} galões e pagará R${preco_total_combinado:.2f}.")