# def fun(prices):
# 	prices.sort()
#
# 	ans = 0
# 	res = len(prices) %3
# 	#print(res)
# 	for i in range(len(prices)-1, res,-3):
# 		#print(prices[i],prices[i-1],prices[i-2])
# 		ans+=prices[i]
# 		ans+=prices[i-1]
# 	for i in range(res):
# 		ans+=prices[i]
# 	#print(ans)
# 	return ans
#
# fun([100,200,300,400])
# fun([100,100,200,300,400])
# fun([100,100,100,200,300,400])
# fun([100,100,100,200,200,300,400])
def fun(nums,n,m):
	if n== 0:
		return 0
	if n == 1:
		if nums[0]%m==0:
			return 1
		else:
			return 0

	ans=0

	dp = [0] * n
	dp[0] = nums[0]
	if nums[0] % m == 0:
		ans+=1
	for i in range(1, n):
		if m == 0:
			if nums[i] == 0:
				print(nums[i])
				ans += 1
		else:
			if nums[i] % m == 0:
				print(nums[i])
				ans += 1
		dp[i] = dp[i-1] + nums[i]
	for i in range(n-1):
		for j in range(i+1,n):

			summation = dp[j] - dp[i] + nums[i]
			print(nums[i:j+1],summation)

			if m == 0:
				if summation == 0:
					#print(nums[i:j+1],summation)
					ans+=1
			else:
				if summation % m == 0:
					#print(nums[i:j+1],summation)
					ans+=1
	return ans
# def fun(nums,n,m):
# 	if n== 0:
# 		return 0
# 	if n == 1:
# 		if nums[0]%m==0:
# 			return 1
# 		else:
# 			return 0
#
# 	lookup = set()
# 	lookup.add(0)
# 	j = 0
# 	ans=0
# 	for i in range(n):
# 		j+=nums[i]
#
# 		if nums[i]% m != 0 and j % m in lookup:
# 			ans+=1
# 		elif i >=1 and nums[i] % m ==0 and nums[i-1]%m ==0:
# 			ans+=1
#
# 		else:
# 			lookup.add(j%m)
# 	return ans



print('--------',fun([1,2,3,4,5],5,2))
print('--------',fun([1,2,3,4,5],5,2))
print('--------',fun([12,2,1],3,12))
print('--------',fun([12,2],2,6))

print('--------',fun([12,2,34],3,6))

# 	l = 0
# 	r = 1
# 	ans = 0
# 	lookup = {}
# 	#lookup[cubes[0]] = 0
#
# 	for i in range(n):
# 		if cubes[i] not in lookup:
# 			lookup[cubes[i]] = [i]
# 		else:
#
# 			lookup[cubes[i]].append(i)
# 	print(lookup)
#
# fun([1,1,2,1,1,3,3,3],8,1)

#
# def fun(L, n,k):
# 	from collections import defaultdict
#
# 	l = 0
#
# 	ans = 0
#
# 	lookup = defaultdict(int)
#
# 	temp = []
# 	max_freq = 0
# 	max_v = -1
#
# 	for r, v in enumerate(L):
# 		lookup[v] +=1
#
#
# 		if lookup[v] > max_freq:
# 			max_freq = lookup[v]
# 			max_v = v
#
# 		while r-l+1 - max_freq > k:
# 			lookup[L[l]] -=1
# 			l+=1
# 			if max_v == L[l]:
# 				max_freq = lookup[L[l]]
#
#
# 		print(L[l:r+1],max_freq)
# 		ans = max(ans,max_freq)
#
# 	return ans
# print(fun([1,1,2,1,1,3,3,3],8,1))
# print(fun([1,1,2,1,3,1],6,2))
#
# def fun(L, n,k):
# 	from collections import defaultdict
#
# 	l = 0
#
# 	ans = 0
#
# 	lookup = defaultdict(int)
# 	for r, v in enumerate(L):
# 		lookup[v] +=1
# 		while r-l+1 - max(lookup.values()) > k:
# 			lookup[L[l]] -=1
# 			l+=1
# 		#print(L[l:r+1])
# 		ans = max(ans,max(lookup.values()))
# 	return ans

