'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        string = list(s);
        string.reverse();
        return "".join(string);