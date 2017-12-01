class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ""
        for i in range(0,len(strs)):
            if (len(strs[i]) == 0):
                return ""
        else:
            index = 0
            for i in range(0, len(strs[0])):
                for j in range(1, len(strs)):
                    if (strs[j][i] != strs[0][i]) or (i > len(strs[j])):
                        return strs[0][0:index]
                index = index + 1
            return strs[0][0:index]
