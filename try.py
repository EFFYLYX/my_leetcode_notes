def heapTest():
	A = ['-INF']
	lastPointer = 0

	def swap(A,a,b):
		temp = A[a]
		A[a] = A[b]
		A[b] = temp

	def heapInsert(num):
		nonlocal lastPointer

		A.append(num)
		lastPointer+=1

		i=lastPointer

		while i > 1 and A[i//2] > A[i]:
			swap(A,i//2,i)
			i = i//2

	def heapRemoveMin():
		nonlocal lastPointer

		temp = A[1]
		swap(A,1,lastPointer)
		lastPointer-=1

		i = 1

		while i < lastPointer:
			if lastPointer >  2*i+1:
				if A[i] <= A[2*i] and A[i] <= A[2*i+1]:
					return temp
				else:
					j = 2*i
					if A[j+1] < A[j]:
						j+=1
					swap(A,i,j)
					i = j
			else:
				if lastPointer > 2*i:
					if A[i] > A[2*1]:
						swap(A,i,2*i)
				return temp

		return temp



	for num in [4,6,7,9,3]:
		heapInsert(num)
	print(A)
	print('min', heapRemoveMin(), A[:lastPointer + 1])
	print('min', heapRemoveMin(), A[:lastPointer + 1])
	print('min', heapRemoveMin(), A[:lastPointer + 1])
	print('min', heapRemoveMin(), A[:lastPointer + 1])
	print('min', heapRemoveMin(), A[:lastPointer + 1])


heapTest()


def quicksortTest():
	def swap(A,a,b):
		temp = A[a]
		A[a] = A[b]
		A[b] = temp

	A = [3, 2, 4, 1, 1]

	def partition(A,a,b):
		p = A[b]
		l = a
		r = b-1
		while l <=r:
			while l<=r and A[l] <=p:
				l+=1
			while l<=r and A[r] >=p:
				r-=1

			if l<r:
				swap(A,l,r)
		swap(A,l,b)
		return l


	def quickSort(A,a,b):
		if a>=b:
			return

		l = partition(A,a,b)
		quickSort(A,a,l-1)
		quickSort(A,l+1,b)
	quickSort(A,0,len(A)-1)
	print(A)
quicksortTest()
