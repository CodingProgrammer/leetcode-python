class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = [None]
        pmap = { ')':'(', ']':'[', '}':'{' }
        for c in s:
            if c in pmap and pmap[c] == f[len(f) - 1]:
                f.pop()
            else:
                f.append(c)
        return len(f) == 1
