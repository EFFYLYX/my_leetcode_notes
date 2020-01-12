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
	def FindKthToTail(self,k):
		now = self.start_node
		ans = []
		while now != None:
			ans.append(now.val)
			now = now.next
		return ans[::-1][k-1]

'''
5
2
1 2
3 2
5 1
4 5
7 2
3
3
'''

while True:
	try:
		n = int(input())
		# print('n ',n)
		start_node = Node(int(input()))
		# print(start_node.val)
		linkedList = LinkedList(start_node)

		for i in range(n):
			line = input().split()
			num1 = int(line[0])
			num2 = int(line[1])
			# print('x',num1,num2)
			linkedList.insert(num2,num1)
		# print('main',linkedList.print_linkedList())
		print(linkedList.print_linkedList())
		del_num = int(input())
		linkedList.delete(del_num)
		print(linkedList.print_linkedList())

		k = int(input())
		print(linkedList.FindKthToTail(k))

	except:
		break

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
