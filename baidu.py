

def fun1(n):
	ans = 0
	for i in range(1,n+1):
		for j in range(1,n+1):
			temp = lcm(i,j) - gcd(i,j)
			ans = max(ans,temp)
	return ans
def gcd(a,b):
	a,b = (a,b) if a >= b else (b,a)
	while b:
		a,b = b,a%b
	return a



def lcm(a,b):
	return a*b//gcd(a,b)

# print(lcm(3,4))
# print(gcd(2,4))
# print(fun1(5))
# print(fun1(3))

def oper(n,a):
	max_i = 0
	max_num = 0
	for i in range(n):
		if i == max_i:
			max_num = a[i]



		else:
			if max_num < a[i]:
				a[max_i] +=1


				max_num = a[i]
				max_i = i



			else:

				a[i]+=1


	a[max_i]-=n

	return a,max(a)

def fun(n,a):
	max_ = max(a)
	if max_ < n:
		return 0
	ans = 1
	a,max_ = oper(n,a)
	print(a)
	while max_ >= n:
		a,max_ = oper(n,a)
		ans+=1
		print(a)
	return ans



	# print(a,max_i,a[max_i])
	# while a[max_i] >= n:
	# 	a,max_i = oper(n,a)
	# 	ans+=1
	# 	print(a, max_i,a[max_i])
	# return ans





print(fun(3,[1,0,3]))
print(fun(3,[1,4,3]))
print(fun(4,[1,4,3,4]))

