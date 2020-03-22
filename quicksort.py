def quicksortTest():
	def swap(A,a,b):
		temp = A[a]
		A[a] = A[b]
		A[b] = temp

	#A = [4,6,7,9,3]
	A= [3,2,4,1,1]

	def partition(A,a,b):

		p = A[b]
		l = a
		r = b-1

		while l <= r:
			while l <= r and A[l] <=p:
				l+=1
			while l<=r and A[r] >=p:
				r-=1

			if l< r:

				swap(A,l,r)

		swap(A,l,b)

		return l

	def quicksort(A,a,b):
		if a >= b:
			return

		l = partition(A,a,b)

		quicksort(A,a,l-1)
		quicksort(A,l+1,b)

	quicksort(A,0,len(A)-1)
	print(A)
quicksortTest()