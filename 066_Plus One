class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        digits[l - 1] += 1
        for i in range(l - 1, -1, -1):
            if 10 == digits[i]:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0,1)
                else:
                    digits[i] = 0
                    digits[i - 1] += 1
        return digits