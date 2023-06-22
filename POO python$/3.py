class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def cal_area(self):
        return self.largura * self.altura
    
    def cal_peri(self):
        return 2 * (self.altura + self.largura)
    
retangulo = Retangulo(10, 10)

area = retangulo.cal_area()
perimetro = retangulo.cal_peri()

print(f"A área do retângulo é {area}")
print(f"O perímetro do retângulo é {perimetro}")
