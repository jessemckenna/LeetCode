'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        n = len(s)
        for i in range(n):
            if s[i] in parentheses:
                # s[i] is a key in |parentheses|, i.e. an opening parenthesis
                stack.append(s[i])
            elif not stack:
                # No opening parenthesis is available to match with s[i]
                return False
            else:
                # s[i] is either a closing parenthesis or an invalid character
                lastOpeningParenthesis = stack.pop()
                if s[i] != parentheses[lastOpeningParenthesis]:
                    # s[i] does not match the last opening parenthesis
                    return False

        if stack:
            # Unmatched parentheses are left over
            return False

        return True