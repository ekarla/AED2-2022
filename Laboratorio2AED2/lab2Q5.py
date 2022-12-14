from math import ceil

def mergesort(lista):
    lista.sort()

monstros =  eval(input())
danos = []

for energy, forca in monstros:
    golpes = ceil(energy/40) - 1
    dano_causado = golpes * forca
    danos.append(dano_causado)

mergesort(danos)

vitorias = 0
energy = 100

for d in danos:
    energy -= d
    if energy > 0:
        vitorias += 1
    else:
        energy = 0
        break
         
print(vitorias,energy)