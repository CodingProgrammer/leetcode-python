class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if 0 == l:
            return 0
        j = 0
        s = s[::-1]
        for i in range(0,l):
            if s[i] != ' ':
                j += 1
            else:
                if j != 0:
                    break
                else:
                    continue
        return j