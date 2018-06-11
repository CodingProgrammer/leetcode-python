class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bucket = {}
        for i, num in enumerate(nums):
            if target - num in bucket:
                return bucket[target - num], i
            bucket[num] = i
