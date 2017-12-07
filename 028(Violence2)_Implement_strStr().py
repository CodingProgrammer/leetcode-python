class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        s1 = len(haystack)
        s2 = len(needle)
        if not needle:  
            return 0  
        if s1 < s2:
            return -1
        for i in range(s1 - s2 + 1):
            j = 0
            k = i
            while j < s2 and haystack[k] == needle[j]:
                j += 1
                k += 1
            if j == s2:
                return i
        return -1
