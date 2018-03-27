'''
Given an array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
'''

class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		length = len(nums)

		if length == 0:
			return None

		if length == 1: 
			return nums[0]

		nums.sort()
		for i in range(0, length - 1, 2): # examine pairs
			if nums[i] != nums[i + 1]: # find number that doesn't match its pair
				return nums[i] # single number found

		if length % 2 != 0: # check for a single element remaining at the end
			return nums[length - 1]

		return None # all numbers match their neighbor, not found