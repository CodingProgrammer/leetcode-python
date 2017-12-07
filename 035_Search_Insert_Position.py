class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange(0, len(nums)):
            if target == nums[i]:
                return i
        nums.append(target)
        nums.sort()
        for i in xrange(0, len(nums)):
            if target == nums[i]:
                return i
