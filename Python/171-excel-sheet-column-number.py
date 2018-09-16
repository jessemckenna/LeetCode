'''
Given a column title as it appears in an Excel sheet, return its corresponding 
column number.

For example:
	A -> 1
	B -> 2
	C -> 3
	...
	Z -> 26
	AA -> 27
	AB -> 28 
	...

Example 1:
	Input: "A"
	Output: 1

Example 2:
	Input: "AB"
	Output: 28

Example 3:
	Input: "ZY"
	Output: 701
'''

class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		ASCII_CAPITAL_A = ord('A')
		n = len(s)
		result = 0
		for i in range(n):
			result += 26**(n - i - 1) * (ord(s[i]) - ASCII_CAPITAL_A + 1)

		return result