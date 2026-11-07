import math

def imprimir(num):
    print("*" * num)

    
def somar():
    a = float(input('Primeiro número:'))
    b = float(input('Segundo número:'))
    return a + b


def dividir():
    a = float(input('Primeiro número:'))
    b = float(input('Segundo número:'))
    if b == 0:
        return f'Não existe divisão com zero'
    return a / b


def raiz_quadrada():
    num = float(input('Primeiro número:'))
    return math.sqrt(num)


def seno():
    angulo = float(input('Digite o ângulo:'))
    radianos = math.pi * angulo / 180
    return math.sin(radianos)
