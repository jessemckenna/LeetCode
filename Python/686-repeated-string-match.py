'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        N = len(A)
        M = len(B)

        if N == 0 or M == 0:
            return -1

        for i in range(N): # iterate over A and find B's starting character
            if A[i] == B[0]:
                mismatch = False
                aMults = 1 # multiples of A needed in order for B to be a substring
                idxA = i
                idxB = 0
                while idxB < M and mismatch == False: # check all characters in B
                    # get index of A
                    if idxA >= N:
                        aMults += 1
                        idxA -= N # loop if reach end of A

                    # compare character in A to character in B
                    if A[idxA] == B[idxB]:
                        idxB += 1
                        idxA += 1
                    else:
                        mismatch = True # no B starting at A[i]; continue iterating over A
                if mismatch == False:
                    return aMults # success; found B by looping over A starting at A[i]

        return -1 # all of A checked, B's starting character never found