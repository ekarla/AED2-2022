def soma_maiores(tupla):
    
    menor_valor = (tupla[1])
    for i in range(1,len(tupla)):
        if menor_valor > (tupla[i]):
            menor_valor = (tupla[i])
    
    soma_valores = (tupla[1]+tupla[2]+tupla[3]) - menor_valor
    
    return (tupla[0],soma_valores)
   
           
    
  
loop = int(input())
placar = []
for i in range(loop):
     
    entrada = eval(input())
    placar.append(soma_maiores(entrada))
    
placar.sort(key = lambda x: x[1], reverse=True)

for i in range(len(placar)):
    print(str(placar[i][0])+": "+str(placar[i][1]))

