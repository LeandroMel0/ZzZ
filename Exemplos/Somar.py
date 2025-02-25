
import random
def ZzZ():
    if(random.random() < 0.5):
        print("ZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ", end="")
        input()
        print("Desculpe, dormi aqui")
    
def Somar(num1, num2):
    ZzZ()
    return num1 + num2

x = 0
y = 0
resultado = 0

print("Digite o primeiro número:")
x = int(input())

print("Digite o segundo número:")
y = int(input())

resultado = Somar(x, y)

print("A soma é: ", resultado)
