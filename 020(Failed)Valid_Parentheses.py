class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        if 1 == len(s):
            return False
        for i in xrange(0,len(s) -1 ):
            if '(' == s[i]:
                if ')' == s[i + 1] :
                    s.pop(i)
                    s.pop(i+1)
                    i = 0
            if '[' == s[i]:
                if ']' == s[i + 1] :
                    s.pop(i)
                    s.pop(i+1)
                    i = 0
            if '{' == s[i]:
                if '}' == s[i + 1] :
                    s.pop(i)
                    s.pop(i+1)
                    i = 0
        if 0 == len(s):
            return True
        else:
            return False
