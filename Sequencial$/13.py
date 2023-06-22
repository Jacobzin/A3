print('Insira sua altura')
a=float(input())
print('Qual seu Sexo (M/F)')
sexo=str(input())
print(sexo)
if sexo>=('M'):
    p=((72.7*a)-58)
    print('Seu peso ideal é %s' %(p))
else:
    p=((62.1*a)-44.7)
    print('Seu peso ideal é %s' %(p))