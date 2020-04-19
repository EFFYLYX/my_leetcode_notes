class Node:
	def __init__(self,val):

		self.val = val
		self.left = None
		self.right = None
def dfs(root):

	#preorder
	WHITE, GRAY = 0, 1
	ans = []
	stack = [(WHITE, root)]
	while stack:
		color, node = stack.pop(-1 gi)
		if node is None:
			continue
		if color == WHITE:

			if node.right:

				stack.append((WHITE, node.right))
			if node.left:
				stack.append((WHITE, node.left))
			stack.append((GRAY, node))
		else:
			ans.append(node.val)
	return ans

def bfs(root):
	WHITE,GRAY = 0,1

	ans = []
	queue = [((WHITE,root))]

	while queue:
		color, node = queue.pop(0)
		if node is None:
			continue
		if color == WHITE:
			if node.left:
				queue.append((WHITE, node.left))
			if node.right:
				queue.append((WHITE, node.right))
			queue.append((GRAY, node))
		else:
			ans.append(node.val)
	return ans



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(dfs(root))
print(bfs(root))



'''
graph

'''

def dfs_graph(m,x,y,n):

	WHITE, GRAY = 0,1
	ans = 0
	stack = [(WHITE,(x,y))]
	while stack:
		color, node = stack.pop(0)

		i,j = node[0],node[1]

		if color == 0:

			if i+1 > -1 and i +1<n and j >-1 and j < n and m[i+1][j] != '#':

				stack.append((WHITE, (i+1,j)))
			if i - 1 > -1 and i - 1 < n and j > -1 and j < n and m[i-1][j] != '#':
				stack.append((WHITE,(i-1,j)))
			if i > -1 and i < n and j+1 > -1 and j+1 < n and m[i][j+1] != '#':
				stack.append((WHITE, (i, j+1)))
			if i > -1 and i < n and j-1 > -1 and j -1< n and m[i][j-1] != '#':
				stack.append((WHITE, (i, j- 1)))

			stack.append((1,(i,j)))

		else:

			if m[i][j].isnumeric():
				ans+= int(m[i][j])
			m[i][j] = '#'
	return ans
m = [['.', '.', '1', '.', '#', '.'], ['2', '#', '#', '3', '#', '8'], ['.', '#', '.', '#', '#', '.'], ['.', '#', '6', '#', '9', '.'], ['4', '#', '#', '#', '.', '.'], ['.', '.', '7', '.', '.', '5']]
x,y = 0,0
n = 6
ans = dfs_graph(m,x,y,n)
print('dfs_graph',ans)


def bfs_graph(m,x,y,n):

	WHITE, GRAY = 0,1
	ans = 0
	queue = [(WHITE,(x,y))]
	while queue:
		color, node = queue.pop(-1)

		i,j = node[0],node[1]

		if color == 0:

			if i+1 > -1 and i +1<n and j >-1 and j < n and m[i+1][j] != '#':

				queue.append((WHITE, (i+1,j)))
			if i - 1 > -1 and i - 1 < n and j > -1 and j < n and m[i-1][j] != '#':
				queue.append((WHITE,(i-1,j)))
			if i > -1 and i < n and j+1 > -1 and j+1 < n and m[i][j+1] != '#':
				queue.append((WHITE, (i, j+1)))
			if i > -1 and i < n and j-1 > -1 and j -1< n and m[i][j-1] != '#':
				queue.append((WHITE, (i, j- 1)))

			queue.append((1,(i,j)))

		else:

			if m[i][j].isnumeric():
				ans+= int(m[i][j])
			m[i][j] = '#'
	return ans
m = [['.', '.', '1', '.', '#', '.'], ['2', '#', '#', '3', '#', '8'], ['.', '#', '.', '#', '#', '.'], ['.', '#', '6', '#', '9', '.'], ['4', '#', '#', '#', '.', '.'], ['.', '.', '7', '.', '.', '5']]
x,y = 0,0
n = 6
ans = bfs_graph(m,x,y,n)
print('bfs_graph',ans)

def dfs_graph_recursion(m,x,y,n):
	visit = [ [False for i in range(n)] for j in range(n)]

	rel = 0
	def backtrack(m, x, y, visit):
		# global rel
		nonlocal rel


		if x < 0 or x >= len(m) or y < 0 or y >= len(m[0]) or visit[x][y] or m[x][y] == '#':

			return


		visit[x][y] = True

		if m[x][y].isnumeric():
			rel += int(m[x][y])

		backtrack(m, x - 1, y, visit)
		backtrack(m, x + 1, y, visit)
		backtrack(m, x, y - 1, visit)
		backtrack(m, x, y + 1, visit)

		#visit[x][y] = False


	backtrack(m,x,y,visit)
	return rel


m = [['.', '.', '1', '.', '#', '.'], ['2', '#', '#', '3', '#', '8'], ['.', '#', '.', '#', '#', '.'], ['.', '#', '6', '#', '9', '.'], ['4', '#', '#', '#', '.', '.'], ['.', '.', '7', '.', '.', '5']]
x,y = 0,0
n = 6
print(dfs_graph_recursion(m,x,y,n))


def bfs_hasPath( maze, start, destination) -> bool:
	directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 定义上下左右四个方向
	m = len(maze)  # 获取矩阵大小
	n = len(maze[0])

	queue = [(start[0], start[1])]  # 构造队列，并将起始位置包含其中
	maze[start[0]][start[1]] = -1  # -1表示该点已经过遍历，防止循环

	while queue:
		i, j = queue.pop(0)  # 弹出坐标值i,j
		# 如果坐标为终点坐标，返回True，程序结束
		if i == destination[0] and j == destination[1]:
			return True
		for dx, dy in directions:  # 对四个方向进行遍历
			x, y = i, j
			while 0 <= x + dx < m and 0 <= y + dy < n and (maze[x + dx][y + dy] == 0 or maze[x + dx][y + dy] == -1):
				# 当x,y坐标合法，并且对应值为0或-1时
				x = x + dx  # 继续前进，模拟小球的滚动过程
				y = y + dy  # 其中0为空地，而-1为之前遍历过的空地
			if maze[x][y] != -1:  # 如果该点的值不为-1，即未遍历过
				maze[x][y] = -1  # 置为1
				queue.append((x, y))  # 并将其坐标添加到队列中

			# 如果遍历所有可能性都无法达到目的地
	return False  # 返回False


def dfs_hasPath( maze, start, destination) -> bool:
	directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 定义上下左右四个方向
	m = len(maze)  # 获取矩阵大小
	n = len(maze[0])

	# 构造dfs函数，其返回值为bool值
	def dfs(m, n, maze, x, y, directions, destination):
		maze[x][y] = -1  # -1表示该点已经过遍历，防止循环
		# 如果坐标为终点坐标，返回True
		if x == destination[0] and y == destination[1]:
			return True

		res = False
		i, j = x, y  # 保存坐标值
		for dx, dy in directions:  # 对四个方向进行遍历
			x, y = i, j
			while 0 <= x + dx < m and 0 <= y + dy < n and (maze[x + dx][y + dy] == 0 or maze[x + dx][y + dy] == -1):
				# 当x,y坐标合法，并且对应值为0或-1时
				x = x + dx  # 继续前进，模拟小球的滚动过程
				y = y + dy  # 其中0为空地，而-1为之前遍历过的空地

			if maze[x][y] != -1:  # 如果该点的值不为-1，即未遍历过
				# 进行遍历，并对res和遍历结果取或
				# 有True即为True
				res = res or dfs(m, n, maze, x, y, directions, destination)

		return res  # 返回res

	return dfs(m, n, maze, start[0], start[1], directions, destination)

'''
https://blog.csdn.net/XX_123_1_RJ/article/details/80289719
'''


'''

adjency matrix, find all paths starting from a node
'''
print()
node = 4 # 输入结点数
data = [[0, 1], [1, 2], [2, 3], [0, 2]]  # 输入路径
maps = [[0] * node for _ in range(node)]  # 转换成邻接矩阵（行是开始，列是结束）
for v in data: maps[v[0]][v[1]] = 1
print(maps)

def findAllPath(maps,start):

	ans = 0
	WHITE,GREY = 0,1
	stack = [[WHITE, start]]

	while stack:
		color, top = stack.pop(-1)
		if color == WHITE:
			for i in range(len(maps[top])):
				if maps[top][i] == 1:
					stack.append([WHITE,i])
			stack.append([GREY,top])
		else:
			ans+=1
print()
node = 4 # 输入结点数
data = [[0, 1], [1, 2], [2, 3], [0, 2]]  # 输入路径
maps = [[0] * node for _ in range(node)]  # 转换成邻接矩阵（行是开始，列是结束）
for v in data: maps[v[0]][v[1]] = 1
print(maps)
import copy
for i in range(node):
	print(i, findAllPath(copy.deepcopy(maps),i))
	#dAllPath(copy.deepcopy(maps),i)
