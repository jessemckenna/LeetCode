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
		
		if b == 0:
			return a
		if a == 0:
			return b

		# bitwise XOR: partial solution before carrying digits
		partialSolution = a ^ b

		# bitwise AND: digits that need carrying (i.e. 1 digits in both numbers)
		digitsToCarry = a & b

		# left-shift toCarry by 1: carried digits to be added to solution
		carriedDigits = digitsToCarry << 1

		# recursively call until all carried digits have been correctly placed,
		# i.e. continue until carriedDigits == 0
		return self.getSum(partialSolution, carriedDigits)