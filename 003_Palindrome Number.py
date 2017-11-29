class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tem = '%d' %x
        tem = tem[::-1]
        tem = re.sub("\D", "", tem)
        a = int(tem)
        if (x == a):
            return True
        else:
            return False
