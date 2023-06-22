##Crie uma classe chamada “Matematica”. Nessa
##classe, implemente os métodos “somar”,
##“subtrair”, “multiplicar” e “dividir”. Cada um
##desses métodos deverá receber 2 inteiros como
##parâmetro e imprimir o respectivo resultado.


class Matematica:
    def somar(self, a, b):
        resultado = a + b
        print(f"O resultado desta soma é {resultado}")
    def subtrair(self, a, b):
        resultado = a - b
        print(f"O resultado da subtração é {resultado}")
    def mult(self, a, b):
        resultado = a * b
        print(f"O resultado da multiplicação é {resultado}")
    def dividir(self, a, b):
        resultado = a / b
        print(f"O resultado da divisão é {resultado}")

mat = Matematica()

mat.somar(1, 2)
mat.subtrair(4, 2)
mat.mult(100, 200)
mat.dividir(4, 2)

    