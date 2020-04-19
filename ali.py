def s2tBfs(s,t):
	if len(s) != len(t):
		return -1

	if set(s) != set(t):
		return -1
	lookup = dict()
	ans = []
	queue = [(s, 0)]

	while queue:
		top, step = queue.pop(0)
		#print(top,'******')

		for i in range(len(top)):
			transform = top[:i] + top[i + 1:] + top[i]

			#print(transform)
			if transform == t:

				if transform not in lookup:
					lookup[transform] = step+1
					ans.append(step + 1)
				else:
					if  lookup[transform] > step+1:
						lookup[transform] = step + 1
						ans.append(step + 1)
					else:
						break
			else:
				if transform not in lookup:
					lookup[transform] = step+1
					queue.append([transform,step+1])
				else:
					if lookup[transform] > step+1:
						lookup[transform] = step+1
						queue.append([ transform, step + 1])
	print(ans)

	if t in lookup:
		return lookup[t]
	return -1
#print(s2tBfs("acdk", "ckad"))


def s2t(s, t):
	if len(s) != len(t):
		return -1

	if set(s) != set(t):
		return -1
	lookup = dict()
	ans = []

	def backtrack(s, t, step):

		if s == t:
			ans.append(step)

			# lookup.remove(s)
			return
		# print(s,t,step,'--------')
		for i in range(len(s)):
			transform = s[:i] + s[i + 1:] + s[i]
			# print(transform)

			if transform not in lookup:
				# print(s, transform)

				lookup[transform] = step

				backtrack(transform, t, step + 1)
			else:
				if lookup[transform] > step:
					lookup[transform] = step
					backtrack(transform, t, step + 1)

	backtrack(s, t, 0)
	print(ans)
	if t in lookup:
		return lookup[t] + 1
	return -1

print('s2t=========================')
print(s2t("acdk", "ckad"))
print(s2t("abcd", "bcda"))
print(s2t("abcd", "adcb"))
print(s2t("abcd", "dbca"))
print(s2t("bcbb", "bbbc"))
print(s2t("bccb", "bbbc"))
print()
#
print(s2tBfs("acdk", "ckad"))
print(s2tBfs("abcd", "bcda"))
print(s2tBfs("abcd", "adcb"))
print(s2tBfs("abcd", "dbca"))
print(s2tBfs("bcbb", "bbbc"))
print(s2tBfs("bccb", "bbbc"))

print()

def s2teasy(s, t):
	if len(s) != len(t):
		return (-1)

	if set(s) != set(t):
		return (-1)
	# sorted(s)
	# sorted(t)
	# for i in range(len(s)):
	# 	if s[i] != t[i]:
	# 		return -1

	idx = 0
	for i in range(len(s)):
		if s[i] == t[idx]:
			idx += 1
	return (len(t) - idx)


print(s2teasy("acdk", "ckad"))
print(s2teasy("abcd", "bcda"))
print(s2teasy("abcd", "adcb"))
print(s2teasy("abcd", "dbca"))
print(s2teasy("bcbb", "bbbc"))
print(s2teasy("bccb", "bbbc"))  # 2

'''

题目：第一行输入整数T, 接下来每行输入一个只有0和1组成的二进制字符串，共输入T个字符串。对于每个字符串，可以翻转每个二进制位若干次，如果能够通过翻转变成全0字符串，输出最少翻转次数，否则输出“NO”;
翻转规则：0变成1,1变成0；翻转第i位时将相邻i-1,i+1的位置字符也翻转(i-1,i+1不能越界)
如：011: 翻转第3位变成000，故输出“1”；
01：输出“NO”

0
1

01 no
10 no

000 OK
001 111 000 OK
010 0 10 001 
101->110->000   1 01
001->111->000  0 01

1110 ok
1000 1111 0000
0101 1011 1100 0000

'''
print("反转二进制=========")

def binaryReverse(s):
	def reverse(digit):
		if digit == '0':
			return '1'
		return '0'

	s = [i for i in s]
	length = len(s)

	if length == 1 and s==['0']:
		print(0)
	if length == 0 and s==['1']:
		print(1)
	if length == 2 and (s == ['0', '1'] or s == ['1', '0']):
		print('NO')

	target = '0' * length
	lookup = dict()


	import copy


	WHITE, GREY = 0,1



	lookup[''.join(s)] = 0
	ans = []

	def backtrack(s, t,step):
		nonlocal ans

		if ''.join(s) == t:
			ans.append(step)
			return

		for i in range(length):
			transform = [i for i in s]
			if i == 0:
				transform[i] = reverse(transform[i])
				transform[i+1] = reverse(transform[i+1])

			elif i == length-1:
				transform[i] = reverse(transform[i])
				transform[i - 1] = reverse(transform[i-1])
			else:
				transform[i] = reverse(transform[i])
				transform[i + 1] = reverse(transform[i + 1])
				transform[i - 1] = reverse(transform[i - 1])
			s_transform = ''.join(transform)


			if s_transform not in lookup:
				lookup[s_transform] = step+1
				backtrack(transform, t, step + 1)
			else:
				if lookup[s_transform] > step + 1:
					lookup[s_transform] = step+1

					backtrack(transform,t,step+1)

	backtrack(s,target,0)
	print(ans,lookup[target])


binaryReverse('100')
binaryReverse('101')
binaryReverse('011')

binaryReverse('111111')

binaryReverse('101010000')
def binaryReverseBfs(s):
	def reverse(digit):
		if digit == '0':
			return '1'
		return '0'

	length = len(s)

	if s == '1':
		print(1)
	if s== '0':
		print(0)
	if length == 2 and (s == '01' or s == '10'):
		print('NO')



	import copy

	WHITE, GREY = 0,1

	queue = [[WHITE,s,0]]
	lookup = {s:0}
	target = '0'*length

	ans = []
	#lookup[target] = float('inf')
	while queue:
		color, top,step = queue.pop(0)

		# if color == WHITE:

		for i in range(length):
			listTop = list(top)
			if i == 0:
				listTop[i] = reverse(listTop[i])
				listTop[i+1] = reverse(listTop[i+1])
			elif i==length-1:
				listTop[i] = reverse(listTop[i])
				listTop[i-1] = reverse(listTop[i-1])
			else:
				listTop[i] = reverse(listTop[i])
				listTop[i-1] = reverse(listTop[i-1])
				listTop[i+1] = reverse(listTop[i+1])
			transform = ''.join(listTop)
			if transform == target:

				if transform not in lookup:
					lookup[transform] = step+1
					ans.append(step + 1)
				else:
					if  lookup[transform] > step+1:
						lookup[transform] = step + 1
						ans.append(step + 1)
					else:
						break
			else:
				if transform not in lookup:
					lookup[transform] = step+1
					queue.append([WHITE,transform,step+1])
				else:
					if lookup[transform] > step+1:
						lookup[transform] = step+1
						queue.append([WHITE, transform, step + 1])
			#queue.append([GREY, top,step])
		# else:
		# 	pass
	print(ans,lookup[target])
print('bfs')
binaryReverseBfs('100')
binaryReverseBfs('101')
binaryReverseBfs('011')

binaryReverseBfs('111111')

binaryReverseBfs('101010000')

print()
binaryReverseBfs('000001001')
binaryReverse('000001001')

'''
今天小强从一副扑克牌里拿出来一叠,其中包括A,2,3,…,10各四张,其中A代表1.他从这一叠中抽出一些牌给小明,并告诉小明每次可以按照下列方式打出一些牌:

单牌:一张牌,例如3
对子:数字相同的两张牌,例如77
顺子:数字连续的五张牌,例如A2345
三对:连续三个对子:例如334455
现在小强想知道最少打出多少次牌可以打光手中的牌.
输入描述:

一行是个空格分隔的整数A1,A2,…A10,分别代表牌为A,2,…,10的个数.
0<=A1,A2,…,A10<=4
保证手上至少有一张牌

输出描述:

仅一行一个整数表示答案

示例:

输入:

1 1 1 2 2 2 2 2 1 1

输出

3

说明:

打出三个顺子,分别为:A2345,45678,678910


'''
'''
三年二班的同学们要去郊游了，他们决定所有人都从一个地方出发，但是每个人都要有不同的路线，最终完成一次郊游。所以他们想知道，在它们去的公园里，究竟有多少种不同的路线供选择。

公园可以被描述为一个具有N个结点，M条有向边的图，你要做的任务就是，选择其中某个点，使得其能够产生尽量多的从这个点出发的路线。

提示：此处可以利用node代表结点的总数，结点编号从0到node-1。edge用来描述边。你的程序应该返回路径最多的结点对应的路径数。
注意：所有的边都是有向边！数据输入将保证不包含环路，不包括重复的边。
输入数据示例：
node = 4  edge = {{0, 1}, {1, 2}, {2, 3}, {0, 2}}，包含4条有向边
输出结果：5
示例解释：显然，0号节点应该是起点。对应的5条路线为：
0 1
0 1 2
0 1 2 3
0 2
0 2 3




'''
# print()
# node = 4  # 输入结点数
# data = [[0, 1], [1, 2], [2, 3], [0, 2]]  # 输入路径
# maps = [[0] * node for _ in range(node)]  # 转换成邻接矩阵（行是开始，列是结束）
# for v in data: maps[v[0]][v[1]] = 1
# print(maps)
print("find path==========")
node = 4  # 输入结点数
data = [[0, 1], [1, 2], [2, 3], [0, 2]]  # 输入路径
maps = [[0] * node for _ in range(node)]  # 转换成邻接矩阵（行是开始，列是结束）
for v in data: maps[v[0]][v[1]] = 1
print(maps)


def findPath(maps, start):
	# print(maps)
	ans = 0
	WHITE, GREY = 0, 1
	stack = [[WHITE, start]]

	while stack:
		color, top = stack.pop(-1)
		if color == WHITE:
			for i in range(len(maps[top])):
				if maps[top][i] == 1:
					stack.append([WHITE, i])
			stack.append([GREY, top])
		else:
			ans += 1

	return ans - 1


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


import copy

for i in range(node):
	# print(i, findPath(copy.deepcopy(maps),i))
	a1 = findPath(copy.deepcopy(maps), i)
	path = copy.deepcopy(maps)
	tmppath = FindAllPath(i, node, path)
	print(a1, tmppath)

'''
给定一个数组n，然后给三个长度为n的数组，可以从这三个数组中选出一个长度为n的数组，
第i个位置需要是从给出的三个数组第i个位置选择的，然后要求使这个数组后一项减前一项的绝对值之和最小。
输入示例：：
5 9  5 4  4
4 7  4 10 3
2 10 9 2  3
这里可以选择5 7 5 4 4，所以输出等于|7-5|+|5-7|+|4-5|+|4-4|=5。所以输出就是5。

'''
# n = 5
# l1 = [5, 9, 5, 4, 4]
# l2 = [4, 7, 4, 10, 3]
# l3 = [2, 10, 9, 2, 3]
n = 6
l1 = [5, 9, 5, 4, 3,4]
l2 = [4, 7, 4, 2,10,3]
l3 = [2, 11,10, 9, 2, 3]
L = [l1, l2, l3]
print()

dp = [[float('inf'), float('inf'), float('inf')] for i in range(n)]
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0
prev = -1
print(dp)
for i in range(1,n):
	for j in [0,1,2]:
		for k in [0,1,2]:
			dp[i][j] = min(abs(L[j][i] - L[k][i-1])+ dp[i-1][k],dp[i][j])

print(min(dp[-1]))




A = list(zip(l1, l2, l3))
pre = [l1[0], l2[0], l3[0]]
minsum = [0, 0, 0]
preSum = [0, 0, 0]

for i in range(1, n):
	for row in range(3):
		# 这行代码表示对上面的公式取最小值。
		minsum[row] = min([preSum[num] + abs(A[i][row] - A[i - 1][num]) for num in range(3)])
	# 为了节省空间，我没有开辟一个和输入数组一样大的空间。
	preSum = minsum.copy()
print(min(minsum))


print()
'''

给出一个二维矩阵，这个矩阵的每一行和每一列都是一个独立的等差数列，其中一些数据缺失了，现在需要推理隐藏但是可以被唯一确定的数字，然后对输入的查询进行回答。

输入描述：
第一行，n,m,q分别表示矩阵的行数，列数和查询的条数。
接下来的n行，每行m个数表示这个矩阵，0表示缺失数据。−109≤Aij≤109-10^9≤A_{ij}≤10^9−10 
9
 ≤A 
ij
​	
 ≤10 
9
 
接下来q行，每行两个数字i,j表示对矩阵中第i行第j列的数字进行查询。

输出描述：
如果可以确定该位置的数字，则输出数字，如果不能确定则输出UNKNOWN。

输入示例：
2 3 6
1 0 3
0 0 0
1 1
1 2
1 3
2 1
2 2
2 3

输出示例：
1
2
3
Unknown
Unknown
Unknown

'''
