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

		maxInt = 0x7FFFFFFF # max 32-bit int
		mask = 0xFFFFFFFF # 32-bit number consisting of all 1s, 
						  # used to get last 32 bits of Python's 64-bit integers

		if b == 0:
			if a <= maxInt:
				return a
			else:
				return ~(a ^ mask) # return 32-bit complement
		if a == 0:
			return b

		# bitwise XOR: partial solution before carrying digits
		partialSolution = a ^ b

		# bitwise AND: digits that need carrying (i.e. 1 digits in both numbers)
		digitsToCarry = a & b

		# left-shift toCarry by 1: carried digits to be added to solution
		carriedDigits = digitsToCarry << 1

		partialSolution = partialSolution & mask
		carriedDigits = carriedDigits & mask

		# recursively call until all carried digits have been correctly placed,
		# i.e. continue until carriedDigits == 0
		return self.getSum(partialSolution, carriedDigits)