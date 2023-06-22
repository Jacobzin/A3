print('Digite seu salario/hora')
sal_hora=float(input())
print('Digite as horas totais de trabalho')
qt_hora=float(input())

bruto=sal_hora*qt_hora
ir=bruto*0.11
inss=bruto*0.08
sin=bruto*0.05
liq=bruto-(inss+ir+sin)

print('Salario Bruto= %s ' % (bruto))
print('Você pagou o total de INSS= %s' %(inss))
print('Você pagou o total de Imposto de renda= %s ' %(ir))
print('Você pagou o total de Sindicato= %s' %(sin))
print('Salario liquido= %s' %(liq))