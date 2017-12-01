class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0):
            return ""
        if (len(strs) == 1):
            return strs[0]
        else:
            index = 0
            for i in range(0, len(strs[0])):
                for j in range(1, len(strs)):
                    if i >= len(strs[j]) or  strs[j][i] != strs[0][i]   :
                        return strs[0][0:index]
                index = index + 1
            return strs[0][0:index]
