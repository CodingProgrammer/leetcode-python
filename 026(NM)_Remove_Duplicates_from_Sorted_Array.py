class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 == len(nums):
            return 0
        i = 0
        for j in xrange(1, len(nums) ):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i = i + 1
        return i + 1
