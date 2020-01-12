# def lengthOfLongestSubstring(s):
# 	from collections import defaultdict
# 	lookup = defaultdict(int)
#
# 	i = 0
# 	j = 0
#
# 	ans = 0
# 	counter = 0
# 	while j < len(s):
# 		print('------')
# 		print('outer ', s[i:j + 1])
# 		if lookup[s[j]] > 0:  # 当前字符已经存在
# 			counter += 1  # 窗口准备缩1位 记录有多少个字符出现过1次了
# 		lookup[s[j]] += 1  # 更新当前字符的occurrence
# 		j += 1
#
# 		while counter > 0:  #
# 			print('inner ', s[i:j])
# 			if lookup[s[i]] > 1:  # 首位字符已经出现多次了
# 				counter -= 1
#
# 			lookup[s[i]] -= 1  # 首位字符将不再窗口范围内
# 			i += 1
# 		ans = max(ans, j - i)
# 	return ans

def lengthOfLongestSubstring(s):
	from collections import defaultdict
	lookup = defaultdict(int)

	i = 0
	j = 0

	ans = 0
	counter = 0
	while j < len(s):
		print('------')
		print('outer ', s[i:j + 1])
		if lookup[s[j]] == 1:  # 当前字符已经存在
			counter += 1  # 窗口准备缩1位 记录有多少个字符出现过1次了
		lookup[s[j]] += 1  # 更新当前字符的occurrence
		j += 1

		while counter > 0:  #
			print('inner ', s[i:j])
			if lookup[s[i]] == 2:  # 找到已经出现2次了的首位字符
				counter -= 1

			lookup[s[i]] -= 1  # 首位字符将不再窗口范围内
			i += 1
		ans = max(ans, j - i)
	return ans

'''
3. 无重复字符的最长子串 medium
多个字符，但是各字符的个数只能为1

abcabcbb
------
outer  a
------
outer  ab
------
outer  abc
------
outer  abca
inner  abca
------
outer  bcab
inner  bcab
------
outer  cabc
inner  cabc
------
outer  abcb
inner  abcb
inner  bcb
------
outer  cbb
inner  cbb
inner  bb
3

'''


def lengthOfLongestSubstringTwoDistinct(s):
	from collections import defaultdict
	lookup = defaultdict(int)
	i, j, counter, ans = 0, 0, 0, 0

	while j < len(s):
		print('------')
		print('outer ', s[i:j + 1])

		if lookup[s[j]] == 0: #新的字符，开始  #记录有多少个不同字符
			counter += 1
		lookup[s[j]] += 1
		j += 1

		while counter > 2: # counter = 3 有3个不同字符
			print('inner ', s[i:j])
			if lookup[s[i]] == 1: #找到多余的字符，其他字符应该有多个重复的
				counter -= 1
			lookup[s[i]] -= 1
			i += 1
		ans = max(ans, j - i)
	return ans


'''
159. 至多包含两个不同字符的最长子串 medium
最多包含两个不同的字符，但是各字母的个数不限制

"eceba"

ece

eceb -> ceb
ceba

------
outer  e
------
outer  ec
------
outer  ece
------
outer  eceb
inner  eceb
inner  ceb
------
outer  eba
inner  eba
3

"ccaabbb"
------
outer  c
------
outer  cc
------
outer  cca
------
outer  ccaa
------
outer  ccaab
inner  ccaab
inner  caab
------
outer  aabb
------
outer  aabbb
5

'''
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstringTwoDistinct('eceba'))
print(lengthOfLongestSubstringTwoDistinct("ccaabbb"))


def lengthOfLongestSubstringKDistinct(s, k):
	from collections import defaultdict
	lookup = defaultdict(int)
	start = 0
	end = 0
	max_len = 0
	counter = 0
	while end < len(s):
		if lookup[s[end]] == 0:
			counter += 1
		lookup[s[end]] += 1
		end += 1
		while counter > k:
			if lookup[s[start]] == 1:
				counter -= 1
			lookup[s[start]] -= 1
			start += 1
		max_len = max(max_len, end - start)
	return max_len

'''
340. 至多包含 K 个不同字符的最长子串
'''
print(lengthOfLongestSubstringKDistinct('abcabcbb',1))

'''
76. 最小覆盖子串 hard

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

'''


def minWindow( s, t):
	from collections import defaultdict
	import sys
	lookup = defaultdict(int)
	for c in t:
		lookup[c] += 1
	i, j = 0, 0
	counter = len(t)
	min_length = float('inf')
	ans = ''

	while j < len(s):
		print('------')
		print('outer ', s[i:j + 1],lookup,'counter:',counter)
		if lookup[s[j]] > 0:
			counter -= 1
		lookup[s[j]] -= 1
		j += 1
		while counter == 0:
			print('inner ', s[i:j],lookup,'counter:',counter)
			if min_length > j - i:
				min_length = j - i
				ans = s[i:j]
			if lookup[s[i]] == 0:
				counter += 1
			lookup[s[i]] += 1
			i += 1
	return ans
print(minWindow('ADOBECODEBANC','ABC'))
l = [1,2,3,4]
print(l[0:])