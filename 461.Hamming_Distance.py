'''
Awesome use of XOR ^ 
'''
from itertools import zip_longest
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return(bin(x^y).count('1'))