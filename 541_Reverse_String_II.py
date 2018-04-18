class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        new_s = ''
        for i in range(0, len(s), 2 * k):
            new_s += s[i:i+k][::-1]
            new_s += s[i+k:i+2*k]
        return (new_s)