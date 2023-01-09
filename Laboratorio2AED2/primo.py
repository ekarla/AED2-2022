def primo(n):
	cont = 2
	eh_primo = True
	while (cont < n) and (eh_primo):
		if (n % cont == 0):
			eh_primo = False
		cont += 1
		
	return eh_primo
	
def remove_duplicado(lista):
	lista_triada = []
	for i in lista:
		if i not in lista_triada:
			lista_triada.append(i)
	return lista_triada

tam = int(input())
lista_valores = []
for i in range(tam):
	lista_valores.append(int(input()))

lista_valores_limpos = remove_duplicado(lista_valores)
primos = []
comuns = []
for i in lista_valores_limpos:
	item = i
	if(item > 1):
		valor = primo((i))
		if(valor == True):
			primos.append(valor)
		else:
			comuns.append(valor)
	else:
		comuns.append(item)
			

print("primos:", len(primos))
print("comuns:", len(comuns))