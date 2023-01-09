def max_heapfy(heap, tam, i):
	maior = i
	filho_left = 2 * i + 1
	filho_rigth = 2 * i + 2
	if filho_left < tam and heap[maior] < heap[filho_left]:
		maior = filho_left
			
	if filho_rigth < tam and heap[maior] < heap[filho_rigth]:
		maior = filho_rigth
		
	if maior != i:
		heap[i], heap[maior] = heap[maior], heap[i]
		max_heapfy(heap, tam, maior)
	
def build_max_heap(heap):
	pai = int((len(heap)//2)-1)
	for i in range(pai,-1,-1):
		max_heapfy(heap,len(heap),i)

		
while True:
	vetor = eval(input())
	build_max_heap(vetor)
	
	if len(vetor) == 0:
		break
		
	print(vetor)
	