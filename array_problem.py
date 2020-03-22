'''
1. 两数之和
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''


def twoSum(self, nums, target):
	d = {}
	for i, num in enumerate(nums):
		d[num] = i
	for i, num in enumerate(nums):
		if target - num in d.keys() and d[target - num] != i:
			return [i, d[target - num]]

'''
15. 三数之和
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

固定一个数，双指针找另外两个数
复杂度分析
时间复杂度：O(n2)
sorted: O(nlogn), outer for loop: O(n), inner while loop(two pointers): O(n)
空间复杂度：O(1)


'''


def threeSum(nums):
	nums = sorted(nums)
	length = len(nums)
	ans = []
	# -4 -1 -1 0 1 2

	for n in range(len(nums)-2):
		if n > 0 and nums[n] == nums[n - 1]:
			continue
		if nums[n] > 0:

			return ans
		if nums[n] + nums[n+1] +  nums[n+2] > 0:
			return ans
		if nums[n] + nums[-1] + nums[-2] < 0:
			continue
		i = n + 1
		j = length - 1
		while i < j:

			if i > n + 1 and nums[i] == nums[i - 1]:
				i += 1
				continue
			if j < length - 1 and nums[j] == nums[j + 1]:
				j -= 1
				continue

			summation = nums[n] + nums[i] + nums[j]

			if summation == 0:
				ans.append([nums[n], nums[i], nums[j]])
			if summation < 0:
				i += 1

			else:# summation >=0
				j -= 1
	return ans
print(threeSum([-1, 0, 1, 2, -1, -4]))

'''
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def fourSum( nums, target):
	ans = []
	nums = sorted(nums)
	length = len(nums)
	for n in range(length - 3):


		if n > 0 and nums[n] == nums[n - 1]:
			continue
		if nums[n] + nums[n+1] + nums[n+2]+nums[n+3]> target: # nums[n]过大
			return ans
		if nums[n] + nums[-3] + nums[-2]+nums[-1] < target:#nums[n]过小
			continue

		for i in range(n + 1, length - 2 ):
			j = i + 1
			k = length - 1

			if i > n+1 and nums[i] == nums[i - 1]:
				continue

			if nums[n] + nums[i]+ nums[i+1] + nums[i+2] > target: # nums[n]+nums[i]过大
				break
			if nums[n] + nums[i]+nums[-2] + nums[-1] < target: #nums[n]+nums[i]过小
				continue

			print(n,i,j,k)
			while j < k:
				print(j,k,nums[n], nums[i], nums[j], nums[k])


				if j > i + 1 and nums[j] == nums[j - 1]:
					j += 1
					continue
				if k < length - 1 and nums[k] == nums[k + 1]:
					k -= 1
					continue
				summation = nums[n] + nums[i] + nums[j] + nums[k]

				if summation == target:
					ans.append([nums[n], nums[i], nums[j], nums[k]])

				if summation < target:
					j += 1
				else: # summation >=0
					k -= 1
	return ans
print(fourSum([1, 0, -1, 0, -2, 2],0))
print(fourSum([-1,0,1,2,-1,-4],-1))
print(fourSum([1,-2,-5,-4,-3,3,3,5],-11))

