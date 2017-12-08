class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def nextStr(s):
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

        s = "1"
        while n > 1:
            n -= 1
            s = nextStr(s)
        return s
