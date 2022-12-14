class ponto:
    
   def __init__(self, x, y):
       self._x = x
       self._y = y
       
   def __lt__(self, outro):
    # Sobrecarga do operador <
    return self._x < outro._y

# Leitura da entrada
#entrada = eval(input())

# Crie uma lista vazia e insira os objetos da classe ponto nela
#pontos = []
#for item in entrada:
	# processe...

# Ordene e imprima de acordo com o enunciado

local = ponto(2,1)


print(local._x < local._y)