def func(n):
	if n == 1:
		return 1
	if n == 2:
		return 4  # 2+2
	dp = []
	dp1 = []
	for i in range(n):
		dp.append(0)
		dp1.append(0)
	dp[0] = 1
	dp[1] = 2 + 2
	dp1[0] = 1
	dp1[1] = 2
	help = []

	for i in range(2, n):
		# dp1[i] = dp1[i-1] + dp1[i-2]
		# dp[i] = dp1[i-1]*2 + dp[i-1]
		# dp[i] = dp[i - 1] + (i - 1) + dp[i - 2] + (i)
		if i % 2 == 0:
			dp[i] = dp[i - 1] + (i - 1) + dp[i - 2] + (i)
		else:
			dp[i] = dp[i - 1] + i + dp[i - 2] + (i)
	# # return dp[-1] * 2 + dp[-1]
	print(dp1,dp)
	return dp[-1]


print(func(3))
print(func(4))
print(func(5))
print(func(6))


def unbrella(l):
	if l[0] == 1 or l[0] == 2:
		return 1
	if l[0] == 3:
		return 3


def sheep(line1, line2):
	S = line1[0]
	n = line1[1]
	a = line1[2]
	# S_left = S - (n - 1) * a
	# V_final = sum(line2)
	S_left = S
	V_final = line2[0]

	for i in range(1,n):
		m1 = S_left - a
		m2 = S_left - 2 * a
		if m1 > m2:
			S_left = m1
			V_final+=line2[i]
		else:
			S_left = m2
			V_final += 2*line2[i]

	if V_final > S_left:
		return S_left
	return -1


# while True:
# 	try:
# 		n = int(input())
# 		for i in range(n):
# 			line1 = input().strip().split()
# 			line2 = input().strip().split()
# 			line1 = [int(item) for item in line1]
# 			line2 = [int(item) for item in line2]
# 			# print(line1,line2)
# 			print(sheep(line1, line2))
# 	except:
# 		break

print(2**34 % 1337)
x  = (((2**3 % 1337) ** 10 % 1337) * (2 ** 4 % 1337) ) % 1337
print(x)