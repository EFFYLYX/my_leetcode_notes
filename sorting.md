### heap sort
```python



def fun():
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



```
#### quicksort

```python
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

```

#### mergesort
```python
def merge_sort(l):
    if len(l) == 1:
        return l
    half = len(l) //2
    l1 = merge_sort(l[0:half])
    l2 = merge_sort(l[half:])
    return merge(l1,l2)

def merge(l1,l2):
    i = 0
    j = 0
    ans = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            ans.append(l1[i])
            i+=1
        else:
            ans.append(l2[j])
            j+=1

    if i < len(l1):
        ans.extend(l1[i:])
    if j < len(l2):
        ans.extend(l2[j:])
    return ans

print(merge_sort([7,6,4,5]))
```