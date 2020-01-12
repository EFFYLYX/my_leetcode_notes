
def print_maze(maze):
	for i in maze:
		for j in i:
			print(j, end=' ')
		print()

if __name__ == '__main__':


	while True:
		try:
			m, n = 9,9
			maze = []
			for i in range(m):
				maze.append([])
				for num in input().split(' '):
					maze[i].append(int(num))
			print_maze(maze)



		except:
			break


'''
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
'''