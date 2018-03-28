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

		# moving zeroes one at a time would be O(n^2)
		
		# count the zeroes? but then we need to somehow move the non-zeroes
		
		# iterate until find non-zero, then swap it and continue iterating?
		# could use 2 pointers (one at the 0, one to iterate for a non-0) - O(n)?

		n = len(nums)

		currentZero = 0
		nextNonZero = 0

		# TODO: the below is a draft. needs review, especially index bounds!

		while (currentZero < n):
			if nums[currentZero] != 0:
				currentZero += 1 # iterate until find a 0 value
			else:
				nextNonZero = currentZero + 1
				while nums[nextNonZero] == 0:
					nextNonZero += 1 # iterate until find a non-0 value to swap

				swap(nums[currentZero], nums[nextNonZero])
				currentZero = nextNonZero