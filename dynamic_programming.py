'''
打家劫舍 II
环路，第一个与最后一个相邻，即考虑两种情况的单线打家劫舍，nums[0:-1],nums[1:]
'''


def rob(nums):
	def line_rob(nums): #单线打家劫舍
		# print(nums)
		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			return max(nums)
		dp = [0 for i in range(len(nums))]
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		for i in range(2, len(nums)):
			dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) # 第i家不抢，第i家抢
		# print(nums,dp)
		return dp[-1]

	if len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		return max(nums)
	return max(line_rob(nums[0:-1]), line_rob(nums[1:]))

'''
337. 打家劫舍 III
二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_recursion(root):
            if not root:
                return 0,0
            left,left_prev = rob_recursion(root.left)
            right,right_prev = rob_recursion(root.right)
            #return max(children's value, children'schildren'value + my value), children's value
            return max(left+right, left_prev+right_prev + root.val), left + right
        return rob_recursion(root)[0]
'''
'''
53. 最大子序和

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6
'''
def maxSubArray(nums):
	if len(nums) == 0:
		return 0

	dp = [0 for i in range(len(nums))]
	dp[0] = nums[0]
	for i in range(1,len(nums)):
		dp[i] = max(dp[i-1] + nums[i], nums[i])

	return max(dp)
print(2**31-1,-2**31)

def fun(x):


	y = 0
	sign = 1
	if x < 0:
		sign = -1
		x = -x

	while x:
		if sign == 1:
			if y > 2147483647:
				return 0
		else:
			if y > 2147483648:
				return 0

		last = x % 10
		y = y * 10 + last
		x = x // 10

	if sign == 1:
		if y > 2147483647:
			return 0
	else:
		if y > 2147483648:
			return 0
	return sign * y
print(fun(2147483647))