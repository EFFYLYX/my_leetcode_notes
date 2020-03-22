def swap(A,a,b):
	temp = A[a]
	A[a] = A[b]
	A[b] = temp

def fun():
	A = ['-INF']
	lastPointer = 0


	def heapInsert(num):

		nonlocal lastPointer

		A.append(num)

		lastPointer+=1

		i = lastPointer

		while i > 1 and A[i//2] > A[i]:
			swap(A,i//2,i)
			i = i//2

	def heapRemoveMin():
		nonlocal lastPointer

		temp = A[1]


		A[1] = A[lastPointer]
		lastPointer-=1

		i = 1
		while i < lastPointer:
			if lastPointer >= (2*i+1):#this node has two childs
				if A[i] <= A[2*i] and A[i] <= A[2*i+1]:
					return temp
				else:
					j = 2*i
					if A[2*i] > A[2*i+1]:
						j +=1
					swap(A,i,j)
					i = j
			else:#this node is leaf or has one child
				if lastPointer >= 2*i: # this node has one child
					if A[i] > A[2*i]:
						swap(A,i,2*i)
				return temp
		return temp #lastPointer = 0


	for num in [4,6,7,9,3]:
		heapInsert(num)
	print(A)

	print('min',heapRemoveMin(),A[:lastPointer+1])
	print('min',heapRemoveMin(),A[:lastPointer+1])
	print('min', heapRemoveMin(), A[:lastPointer+1])
	print('min', heapRemoveMin(), A[:lastPointer + 1])
	print('min', heapRemoveMin(), A[:lastPointer + 1])


fun()

'''
['-INF', 3, 4, 7, 9, 6]
min 3 ['-INF', 4, 6, 7, 9]
min 4 ['-INF', 6, 9, 7]
min 6 ['-INF', 7, 9]
min 7 ['-INF', 9]
min 9 ['-INF']

'''


