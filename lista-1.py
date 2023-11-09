nomes = ['Alice', 'Yuri Gagarin', 'Vescheslav Ulyanovsky',
         'Carolina Herrera', 'Sergey Korolev']

print(nomes)

agenda = {'Yuri Gagarin': '+5 555 - 5 - 222 - 888', 'Lyudmila Pavlychenko': '+5 434 - 5 - 392 - 666'}

print(agenda)

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

#print(calcular_media())


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

fila = [1, 2, 3, 4, 5]

fila.pop(0)

fila.append(6)

#exemplos da revisão slide!!!!