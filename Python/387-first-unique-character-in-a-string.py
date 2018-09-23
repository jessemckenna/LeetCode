'''
Given a string, find the first non-repeating character in it and return its 
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        count = [0] * 26
        firstIdx = [None] * 26
        a = ord('a')

        for i in range(n):
            current = ord(s[i]) - a
            count[current] += 1
            if firstIdx[current] == None:
                firstIdx[current] = i

        firstUniqueIdx = n
        for i in range(26):
            if count[i] == 1 and firstIdx[i] < firstUniqueIdx:
                firstUniqueIdx = firstIdx[i]

        if firstUniqueIdx == n:
            return -1
        else:
            return firstUniqueIdx