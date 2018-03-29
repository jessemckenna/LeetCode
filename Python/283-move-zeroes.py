'''
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""

		n = len(nums)
		if n <= 1:
			return

		### bubble-sort implementation: O(n^2) ###	
		# swaps = 1
		# while (swaps > 0):
		# 	swaps = 0
		# 	for i in range(n - 1):
		# 		if nums[i] == 0:
		# 			nums[i], nums[i + 1] = nums[i + 1], nums[i] # swap i, i + 1
		# 			swaps += 1

		### two-pointer implementation: O(n) ###
		currentZero = 0
		nextNonZero = 0

		while True:
			while nums[currentZero] != 0: # iterate until find a 0
				currentZero += 1
				if currentZero == n - 1: # end of array reached, no more 0s
					return
			
			if nextNonZero <= currentZero:
				nextNonZero = currentZero + 1

			while nums[nextNonZero] == 0: # iterate until find a non-0 to swap
				nextNonZero += 1
				if nextNonZero == n: # end of array reached, all 0s placed
					return

			nums[currentZero], nums[nextNonZero] = \
					nums[nextNonZero], nums[currentZero] # swap elements