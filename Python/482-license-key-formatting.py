'''
You are given a license key represented as a string S which consists only 
alphanumeric character and dashes. The string is separated into N+1 groups by N 
dashes.

Given a number K, we would want to reformat the strings such that each group 
contains exactly K characters, except for the first group which could be shorter 
than K, but still must contain at least one character. Furthermore, there must 
be a dash inserted between two groups and all lowercase letters should be 
converted to uppercase.

Given a non-empty string S and a number K, format the string according to the 
rules described above.
'''

#class Solution(object):
def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    
    n = len(S)
    if n == 0 or n <= K:
        return S.upper().replace("-", "")
            
    # count number of alphanumeric characters
    alnums = sum(i.isalnum() for i in S)
    hyphens = S.count("-")
    if alnums + hyphens < n:
        print("String contains non-alphanumeric, non-hyphen characters")
        return
    
    # move values to new list
    result = []
    index = 0
    alnumsPlaced = 0
    groupLen = 0
    
    firstGroup = alnums % K
    if firstGroup > 0:
        while groupLen < firstGroup: # create undersized first group if needed
            if S[index].isalnum():
                result.append(S[index].upper())
                groupLen += 1
                alnumsPlaced += 1
            index += 1
        result.append("-")
    
    while alnumsPlaced < alnums: # create subsequent groups
        groupLen = 0
        while groupLen < K:
            if S[index].isalnum():
                result.append(S[index].upper())
                alnumsPlaced += 1
                groupLen += 1
            index += 1
        result.append("-")
    
    result = result[:len(result) - 1] # remove trailing hyphen
    result = ''.join(result)
    return result

print(licenseKeyFormatting("a-a-a-a-", 1))