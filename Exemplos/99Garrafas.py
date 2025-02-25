
import random
def ZzZ():
    if(random.random() < 0.5):
        print("ZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ", end="")
        input()
        print("Desculpe, dormi aqui")
    
garrafas = 99
while True:
    ZzZ()
    if (garrafas > 0):
        ZzZ()
        print(garrafas," garrafas de cerveja na parede, ",garrafas," garrafas de cerveja.")
        print("Tire uma do chão, passe-a para frente.")
        garrafas = garrafas - 1
        print(garrafas," garrafas de cerveja na parede.")
    else:
        ZzZ()
        break
