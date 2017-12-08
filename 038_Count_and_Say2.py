class Solution(object):
    def nextStr(self,s):
        count = 0; ans = ""; tem = s[0]
        for i in xrange(len(s)):
            if s[i] == tem:
                count += 1
            else:
                ans += str(count) + tem
                tem = s[i]
                count = 1
        ans += str(count) + tem
        return ans
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """     
        s = "1"
        while n > 1:
            n -= 1
            s = self.nextStr(s)
        return s
