'''
Calculate the sum of two integers a and b, but you are not allowed to use the 
operator + and -.
'''

class Solution(object):
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		
		# thoughts: consider that remainder is similar to subtraction for small
		# numbers, ex. 5 % 3 = 2, and 5 - 3 = 2.
		# for small numbers, essentially we have x % a = b, and we need x.
		# maybe expand on that concept?