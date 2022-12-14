
def insertionSort(arr):
 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def removeDup(lista):
	lista_triada = []
	for i in lista:
		if i not in lista_triada:
			lista_triada.append(i)
	print(lista_triada)
                

entrada = eval(input())
while entrada != []:
    
    entrada = eval(input())
    #insertionSort(entrada)
    #removeDup(entrada)
    print(type(entrada))
