class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        s1 = len(haystack)
        s2 = len(needle)
        if 0 == s2:
            return 0
        if s1 < s2:
            return -1
        i = 0
        while i < s1:
            if s1 - i < s2:
                return -1
            if haystack[i] == needle[0]:
                j = 1
                while j < s2:
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == s2:
                    return i
            i += 1
        return -1
