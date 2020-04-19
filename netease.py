def fun(m_old, m_new, n):
	# ans = []
	# new = list(range(1,n+1))
	old = list(range(1, n + 1))
	ans = {}
	while m_new:
		cur = m_new.pop(0)
		nu = cur[0]
		choice = cur[1:]
		for c in choice:
			if c in old:
				# print(nu, ' ', c)
				#
				# old.remove(c)
				# break
				if c not in old:
					m_old
				else:
					old.remove(c)
					ans[nu] = c
					break


# print(ans)

n = 3
m_new = [[1, 2, 3, 1], [2, 1, 3, 2], [3, 1, 2, 3]]
m_old = [[1, 1, 2, 3], [2, 1, 2, 3], [3, 1, 2, 3]]
fun(m_old, m_new, n)


def dfs(m,x,y,n):
	print('####')
	WHITE, GRAY = 0,1
	ans = 0
	stack = [(WHITE,(x,y))]
	while stack:
		color, node = stack.pop(0)
		print(node,color==WHITE)
		# if node is None:
		# 	continue
		i,j = node[0],node[1]
		print('--',stack)
		if color == 0:
			print('color==0')
			# if i+1 > -1 and i +1<n and j >-1 and j < n and m[i+1][j] != '#':
			#
			# 	stack.append((WHITE, (i+1,j)))
			# if i - 1 > -1 and i - 1 < n and j > -1 and j < n and m[i-1][j] != '#':
			# 	stack.append((WHITE,(i-1,j)))
			# if i > -1 and i < n and j+1 > -1 and j+1 < n and m[i][j+1] != '#':
			# 	stack.append((WHITE, (i, j+1)))
			# if i > -1 and i < n and j-1 > -1 and j -1< n and m[i][j-1] != '#':
			# 	stack.append((WHITE, (i, j- 1)))
			print(i+1 > -1 and i +1<n and j >-1 and j < n)
			if i+1 > -1 and i +1<n and j >-1 and j < n:
				if  m[i+1][j] != '#':
					stack.append((WHITE, (i+1,j)))
			if i - 1 > -1 and i - 1 < n and j > -1 and j < n :
				if m[i-1][j] != '#':
					stack.append((WHITE,(i-1,j)))
			if i > -1 and i < n and j+1 > -1 and j+1 < n  :
				if m[i][j+1] != '#':
					stack.append((WHITE, (i, j+1)))
			if i > -1 and i < n and j-1 > -1 and j -1< n :
				if m[i][j-1] != '#':
					stack.append((WHITE, (i, j- 1)))
			stack.append((1,(i,j)))
			print('+',stack)
		else:

			#if m[i][j] != '.' and m[i][j] !='#':
			if m[i][j].isnumeric():
				ans+= int(m[i][j])
			m[i][j] = '#'
			print('.',stack)
	print('.......',ans)
	return ans

#
# while True:
# 	try:
# 		n = int(input())
# 		m = []
# 		for i in range(n):
# 			m.append([])
# 			for j in input():
# 				#print(j)
# 				m[i].append(j)
# 		# print(m)
# 		_ = input().split()
# 		x = _[0]
# 		y = _[1]
# 		# print(x,y)
# 		print(m,x,y,n)
# 		ans = dfs(m,x,y,n)
# 		print(ans)
# 	except:
# 		break
#
# # m = [['.', '.', '1', '.', '#', '.'], ['2', '#', '#', '3', '#', '8'], ['.', '#', '.', '#', '#', '.'], ['.', '#', '6', '#', '9', '.'], ['4', '#', '#', '#', '.', '.'], ['.', '.', '7', '.', '.', '5']]
# # x,y = 0,0
# # n = 6
# # ans = dfs(m,x,y,n)
# # print(ans)
# #
# # m =[['1','1'],['1','#']]
# # x,y = 0,0
# # n = 2
# # ans = dfs(m,x,y,n)
# # print(ans)
#
def fun3(data,n):
	# join
	d = {}
	x = {}

	idx = {}
	i_=0
	for da in data:
		# if da[0] not in d:
		# 	d[da[0]] = [da[1]]
		# else:
		# 	d[da[0]].append(da[1])
		if da[1] not in d:
			d[da[1]] = [da[0]]
		else:
			d[da[1]].append(da[0])
		if da[0] not in idx:
			idx[da[0]] = i_
			i_+=1


	#print(d,idx)
	idx_={}
	for i,j in idx.items():
		idx_[j] = i
	nn = i_
	m = [[0 for i in range(nn)] for j in range(nn)]
	#print(m)

	for un,v in d.items():
		#rint(un,v)
		for i in range(len(v)):
			for j in range(i+1,len(v)):
				# print(i,j)
				# print(v[i],v[j])
				# print(idx[v[i]])
				# if v[i] != v[j]:

				y = idx[v[i]]
				z = idx[v[j]]
			# if y != z:
				m[y][z]+=1
				m[z][y]+=1
				#print(v[i], v[j],m[y][z])


	#where
	#print(m)
	ans = []
	for i in range(nn):
		for j in range(nn):
			if m[i][j] >2 and i!=j:
				#print(i,j)
				#print(idx_[i],idx_[j],m[i][j])
				ans.append([idx_[i],idx_[j],m[i][j]])
	ans.sort(key=lambda x:(x[0],x[1]))

	# print(ans)
	for l in ans:
		print(l[0],l[1],l[2])


#
# while True:
# 	try:
# 		n = int(input())
# 		data = []
# 		for i in range(n):
# 			data.append([])
# 			for j in input().split():
# 				data[i].append(j)
# 		#print(n, data)
# 		fun3(data,n)
# 	except:
# 		break
