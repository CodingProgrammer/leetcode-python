class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if 0 == len(nums):
            return 0
        j = 0
        for i in xrange(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
        return j
