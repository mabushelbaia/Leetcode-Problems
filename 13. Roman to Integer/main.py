class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = 0
        roman ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        while i < len(s):
            if i + 1< len(s) and s[i:i+2] in roman:
                ss = ss + roman[s[i:i+2]]
                i = i + 2
            else :
                ss = ss + roman[s[i]]
                i = i + 1
        return ss