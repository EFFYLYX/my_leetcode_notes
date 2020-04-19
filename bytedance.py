# def fun1(a, b, n):
# 	delta = None
# 	prev = -1
# 	for i in range(n):
# 		if a[i] != b[i]:
# 			if not delta:
# 				delta = b[i] - a[i]
# 				prev = i
# 			else:
# 				if b[i] - a[i] != delta:
# 					return False
# 				if i != prev+1:
# 					return False
# 				prev = i
# 	return True
#
#
# while True:
# 	try:
# 		t = int(input())
# 		for i in range(t):
# 			n = int(input())
# 			a_ = input().split()
# 			b_ = input().split()
# 			a, b = [], []
# 			for j in range(n):
# 				a.append(int(a_[j]))
# 				b.append(int(b_[j]))
# 			# print(a, b)
# 			if fun1(a, b, n):
# 				print('YES')
# 			else:
# 				print('NO')
# 	except:
# 		break
# '''
# 3
# 6
# 3 7 1 4 1 2
# 3 7 3 6 3 2
# 5
# 1 1 1 1 1
# 1 2 1 3 1
# 5
# 1 1 1 1 1
# 1 2 1 3 1
# '''
# def fun2(n,nums):
# 	ans = 0
# 	for i in range(n-2, -1,-1):
# 		if nums[i+1] < nums[i]:
# 			x = (nums[i] -1) // nums[i+1]
# 			ans+=x
# 			nums[i] //= (x+1)
# 	return ans
# while True:
# 	try:
# 		n = int(input())
# 		nums_ = input().split()
# 		nums = []
# 		for i in range(n):
# 			nums.append(int(nums_[i]))
# 		#print(n,nums)
# 		print(fun2(n,nums))
# 	except:
# 		break
# print(fun2(5,[3,12,13,9,12]))
# #fun2(5,[3,5,13,9,12])
# '''
# 5
# 3 5 13 9 12
# [3,12,13,9,12]
#
# '''

# def fun3(n,m,a,b):
# 	ans = 0
# 	a.sort()
# 	b.sort()
# 	l = 0
# 	r = n-1
# 	while b:
# 		top = b.pop(0)
# 		tmp = top
#
# 		#print(top,a[l])
# 		if l < n:
# 			while l < n and top >= a[l]:
# 				top = tmp - a[l]
# 				l+=1
# 			ans+=top
# 		else:
# 			ans+=(top-a[-1])
# 		#print('----',ans)
# 	#print('00000')
# 	if b:
# 		ans+=b.pop(0)
# 	return ans
#
# #
# while True:
# 	try:
# 		l1 = input().split()
# 		l2 = input().split()
# 		l3 = input().split()
#
# 		n, m = int(l1[0]), int(l1[1])
# 		a = []
# 		for i in range(n):
# 			a.append(int(l2[i]))
# 		b = []
# 		for i in range(m):
# 			b.append(int(l3[i]))
# 		# print(n,m,a,b)
# 		print(fun3(n, m, a, b))
# 	except:
# 		break
#
# #print(fun3(3,4 ,[50, 100, 200],[99, 199, 200, 300]))

def fun4(n, H):
	# ans = []
	# for i, h in enumerate(H):
	# 	l,r= i-1,i+1
	# 	see = 0
	# 	while l >=0 and H[l] <= h:
	# 		see+=1
	# 		l-=1
	# 	while r < n and H[r] <=h:
	# 		see+=1
	# 		r+=1
	# 	ans.append(see)
	# return ans
	left = [0 for i in range(n)]
	right = [0 for i in range(n)]

	# stack = [(n-1, H[n-1])]
	max_l = H[-1]
	min_l = H[-1]
	for i in range(n-2,-1,-1):
		if H[i] >H[i+1]:
			left[i] = left[i+1]+1
		# else:


	# stack = [(0,H[0])]
	# stackcount = 0
	#
	# max_right = 0
	# for i, h in enumerate(H):
	# 	if i == 0:
	# 		continue
	# 	if stack:
	# 		top_i,top_h = stack[0]
	#


	# 	print('s',stack,right)
	# 	if stack:
	# 		if h < H[stack[-1][0]]:
	# 			stack.append(i)
	# 			# stackcount+=1
	# 		else:
	# 			idx,top = stack.pop(0)
	# 			right[idx] = i-idx
	# 			stack.append(i)
	# 	else:
	# 		stack.append(i)
	# 		# stackcount += 1
	# print(right)

fun4(5,[8,2,2,4,6])
#
# while True:
# 	try:
# 		t= int(input())
# 		for i in range(t):
# 			n = int(input())
# 			l_ = input().split()
# 			l = []
# 			for j in range(n):
# 				l.append(int(l_[j]))
# 			print(n,l)
# 			#print(fun4(n,l))
# 			ans = fun4(n,l)
# 			#print(ans)
# 			print(' '.join([str(num) for num in ans]))
#
# 	except:
# 		break
