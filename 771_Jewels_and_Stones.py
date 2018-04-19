class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for each_c in J:
            result += S.count(each_c)
        return (result)
        