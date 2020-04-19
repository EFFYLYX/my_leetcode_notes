# def heapTest():
# 	A = ['-INF']
# 	lastPointer = 0
#
# 	def swap(A,a,b):
# 		temp = A[a]
# 		A[a] = A[b]
# 		A[b] = temp
#
# 	def heapInsert(num):
# 		nonlocal lastPointer
#
# 		A.append(num)
# 		lastPointer+=1
#
# 		i=lastPointer
#
# 		while i > 1 and A[i//2] > A[i]:
# 			swap(A,i//2,i)
# 			i = i//2
#
# 	def heapRemoveMin():
# 		nonlocal lastPointer
#
# 		temp = A[1]
# 		swap(A,1,lastPointer)
# 		lastPointer-=1
#
# 		i = 1
#
# 		while i < lastPointer:
# 			if lastPointer >  2*i+1:
# 				if A[i] <= A[2*i] and A[i] <= A[2*i+1]:
# 					return temp
# 				else:
# 					j = 2*i
# 					if A[j+1] < A[j]:
# 						j+=1
# 					swap(A,i,j)
# 					i = j
# 			else:
# 				if lastPointer > 2*i:
# 					if A[i] > A[2*1]:
# 						swap(A,i,2*i)
# 				return temp
#
# 		return temp
#
#
#
# 	for num in [4,6,7,9,3]:
# 		heapInsert(num)
# 	print(A)
# 	print('min', heapRemoveMin(), A[:lastPointer + 1])
# 	print('min', heapRemoveMin(), A[:lastPointer + 1])
# 	print('min', heapRemoveMin(), A[:lastPointer + 1])
# 	print('min', heapRemoveMin(), A[:lastPointer + 1])
# 	print('min', heapRemoveMin(), A[:lastPointer + 1])
#
#
# heapTest()
#
#
# def quicksortTest():
# 	def swap(A,a,b):
# 		temp = A[a]
# 		A[a] = A[b]
# 		A[b] = temp
#
# 	A = [3, 2, 4, 1, 1]
#
# 	def partition(A,a,b):
# 		p = A[b]
# 		l = a
# 		r = b-1
# 		while l <=r:
# 			while l<=r and A[l] <=p:
# 				l+=1
# 			while l<=r and A[r] >=p:
# 				r-=1
#
# 			if l<r:
# 				swap(A,l,r)
# 		swap(A,l,b)
# 		return l
#
#
# 	def quickSort(A,a,b):
# 		if a>=b:
# 			return
#
# 		l = partition(A,a,b)
# 		quickSort(A,a,l-1)
# 		quickSort(A,l+1,b)
# 	quickSort(A,0,len(A)-1)
# 	print(A)
# quicksortTest()

ans = []


def backtrack(l):  # l=[1,2,3]
	if len(l) == 1:  # l=[1]

		return [l]

	temp = []
	#print(l)
	for i in range(len(l)):

		res = backtrack(l[:i] + l[i + 1:])

		for r in res:
			temp.append(r + [l[i]])

	return temp


print(backtrack([1,2,3]))

A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

i, j = 0, 0
while i < len(A) and j < len(B):
	if A[i] > B[j]:
		# A[i],B[j] = B[j],A[i]
		A.insert(i, B[j])
		i += 1
		j += 1
	else:
		i+=1


	# while B[j] <=

if i >= len(A):
	for val in B[j:]:
		A.append(val)
print(A)

import copy


def FindAllPath(one, node, path):
	st = [[one, one, -1]]  # 第一个值表示，已经入栈的结点，第二个值表示下一个结点的起始位置，最后一个值表示下一个结点已经扩展了几次
	sumpath = 0  # 记录路径数
	while st:  # 如果不为空
		i, j, di, find = st[-1][0], st[-1][1], st[-1][2], 0  # 获取栈顶信息
		i1, j1 = -1, -1  # 记录下一步可走的坐标
		while di < node - 1 and find == 0:
			di += 1  # 下一个结点
			i1, j1 = j, di  # 新的开始
			if path[i1][j1] == 1: find = 1
		if find == 1:  # 找到新结点，入栈
			st[-1][2] = di  # 更新已经判断过的结点
			st.append([i1, j1, -1])  # 添加先的可走路径
			path[i1][j1] = 0  # 把路径标记为不可走
		else:
			path[st[-1][0]][st[-1][1]] = 1  # 恢复可走路径
			sumpath += 1  # 记录出栈几次，也就是有几条路径
			st.pop()  # 出栈
	return sumpath - 1  # 第一个入栈的不算要减去1


if __name__ == '__main__':
	node = 4  # 输入结点数
	data = [[0, 1], [1, 2], [2, 3], [0, 2]]  # 输入路径
	maps = [[0] * node for _ in range(node)]  # 转换成邻接矩阵（行是开始，列是结束）
	for v in data: maps[v[0]][v[1]] = 1

	maxpath, I = -1, -1  # 获取最大路径数, 和选择的位置
	for i in range(node):  # 每个结点获取一次最大路径数
		path = copy.deepcopy(maps)

		tmppath = FindAllPath(i, node, path)
		print(i,tmppath)
		if tmppath > maxpath:
			maxpath, I = tmppath, i

	print('选择开始位置:', I, '最大路径数:', maxpath)


