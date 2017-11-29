class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '0':
            return 0
        else:
            d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
            res = 0
            for i in range(0,len(s)):
                if i == 0 or d[s[i]] <= d[s[i-1]]:
                    res += d[s[i]]
                else:
                    res += d[s[i]] - 2 *  d[s[i-1]]
        return res
