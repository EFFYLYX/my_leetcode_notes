'''
nowcoder 名字的漂亮度
'''

'''
def func(s):
	d = {}

	for i in s:
		if i.lower() in d:
			d[i.lower()] += 1
		else:
			d[i.lower()] = 1

	d = sorted(d.items(), key=lambda x: x[1], reverse=True) #字典排序


	scores = list(range(26,0,-1))

	ans = 0
	for i,tuple in enumerate(d):
		ans+=tuple[1]*scores[i]
	print(ans)



while True:
	try:
		n = int(input())
		for i in range(n):
			func(input())
	except:
		break
'''

'''
nowcoder 插值法
4 n
23 5
46 25   (程序中用KEY和VALUE来保存他们)
46 32  (舍弃该对数值)
82 46  (应用82和46进行比较)

题目的意思是，连续的意思是这样的：
3 5
2 3
2 10
10 5
这样，出现了两个key为2的值的，就为重复。
然后，如果是
3 5
2 5
10 5
2 10
这种是不算重复的。
'''
'''
def func(matrix):

	import math
	previous = matrix[0]
	ans = [previous]
	for  l in matrix[1:]:
		if previous[0] == l[0]:
			continue 
		else:
			differ = l[0] - previous[0]

			if differ >1:
				M, A = previous
				N, B = l
				step = math.trunc((B-A)/(N-M) )
				for i in range(differ-1):
					ans.append([ M + i + 1   , A+step* (i +1) ])
				ans.append(l)
				previous = l
			else:

				ans.append(l)
				previous = l

	for i,j in ans:
		print('%d %d'%(i,round(j)))





while True:
	try:
		m,n = input().split()
		m = int(m)
		n = int(n)
		matrix = []
		for i in range(m):
			matrix.append([])
			for j in input().split():
				matrix[i].append(int(j))

		#print(matrix)
		func(matrix)
	except:
		break
'''


'''
5
2
1 2
3 2
5 1
4 5
7 2
3

最后的链表的顺序为 2 7 3 1 5 4

4
2
3 2
4 3
5 2
1 4
3
'''
'''
class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
class LinkedList:
	def __init__(self, node):
		self.start_node = node
	def insert(self,A,B):
		# print(A,B)
		now = self.start_node
		# print(now.val)
		while now != None:

			# print(now.val,A,now.val == A)

			if now.val == A:
				# print('ddd')
				res = now.next
				new_node = Node(B)
				now.next = new_node
				new_node.next = res
				return True
			now = now.next

		return False
	def print_linkedList(self):
		now = self.start_node
		ans = []
		while now != None:
			# print(now.val)
			ans.append(str(now.val))
			now = now.next
		# print('ans',ans,' '.join(ans))
		return ' '.join(ans)
	def delete(self,A):
		now = self.start_node
		if now.val == A:
			new_node = Node(A)
			new_node.next = now.next
			self.start_node = new_node
			return True
		previous= now
		now = now.next
		while now != None:
			if now.val == A:

				previous.next = now.next
				return True
			previous = now
			now = now.next
		return False

while True:
	try:
		n = int(input())

		start_node = Node(int(input()))
		# print(start_node.val)
		linkedList = LinkedList(start_node)

		for i in range(n):
			line = input().split()
			num1 = int(line[0])
			num2 = int(line[1])
			# print(num1,num2)
			linkedList.insert(num2,num1)
		# print('main',linkedList.print_linkedList())

		del_num = int(input())
		linkedList.delete(del_num)
		print(linkedList.print_linkedList())

	except:
		break
'''
'''
while True:
	try:
		n = int(input())

		res = [input()]
		for i in range(n):
			line = input().split()
			num1 = line[0]
			num2 = line[1]
			res.insert(res.index(num2)+1, num1)
		rm = input()
		res.remove(rm)
		# print(res)
		print(' '.join(res))



	except:
		break
'''

'''
            1

         1  1  1

      1  2  3  2  1

   1  3  6  7  6  3  1

1  4  10 16 19  16 10  4  1

以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。

求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3。
'''
def func(n):
	if n == 0:
		return -1
	if n== 1 or n==2:
		return -1
	# print(n)
	dp = [[1],[1,1,1]]
	for i in range(3, n+1):
		# print(i)
		dp.append([1])
		num = 2 * i - 1 -2
		for j in range(num):
			# print(j,'|',j-1,j,j+1)
			first  = 0
			second = 0
			last = 0
			if j - 1 >=0:
				first = dp[-2][j - 1]

			second = dp[-2][j]
			if j+1 < len(dp[-2]):
				last = dp[-2][j + 1]
			# print(first,second,last,'=',first+second+last)
			dp[-1].append(first + second + last)
		dp[-1].append(1)
	# print(dp)
	for i in dp[-1]:
		if i % 2 ==0:
			return dp[-1].index(i) +1
	return -1

print(func(5))
print(func(4))
print(func(3))