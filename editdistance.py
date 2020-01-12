def editdistance(s1,s2):
	#print(s1,s2)
	dp = []
	for i in range(len(s1)+1):
		dp.append([])
		for j in range(len(s2)+1):
			dp[i].append(0)
	# print(dp)
	for i in range(1,len(s1)+1):
		dp[i][0] = i
	for j in range(1,len(s2)+1):
		dp[0][j] = j
	# print(dp)
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			# print(dp[i][j,s1[i-1],s2[j-1]])
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
	# print(dp)
	return dp[-1][-1]
while True:
	try:
		print(editdistance(input(), input()))
	except:
		break
