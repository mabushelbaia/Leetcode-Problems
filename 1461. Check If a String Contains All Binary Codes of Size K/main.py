class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        se = set()
        for i in range(len(s) - k + 1):
            se.add(s[i:i+k])
        return len(se) ==  2**k

        