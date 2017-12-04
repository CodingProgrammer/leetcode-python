class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = [None]
        pmap = { ')':'(', ']':'[', '}':'{' }
        for c in s:
            if c in pmap :
                if pmap[c] != f.pop() :
                    return False
            else:
                f.append(c)
        return len(f) == 1
