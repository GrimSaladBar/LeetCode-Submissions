class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Original Solution:
        for num in nums:
            if (nums.__contains__(target - num) and nums.index(num) is not nums.index(target-num)):
                return [nums.index(num), nums.index(target - num)]
            elif(nums.__contains__(target - num) and nums.count(num) >= 2):
                return [nums.index(num), nums.index((target - num), nums.index(num) + 1)]
        """
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return [i, nums.index(diff)]
