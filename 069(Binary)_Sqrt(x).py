class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if 0 == x:
            return 0
        i = 1
        j = x / 2 + 1
        while(i <= j):
            center = int((i + j) / 2 )
            if center ** 2 == x:
                return center
            elif center ** 2 > x:
                j = center - 1
            else:
                i = center + 1
        return j