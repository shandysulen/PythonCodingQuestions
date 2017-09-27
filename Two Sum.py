class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        history = {}
        for i in range(len(nums)):
            if nums[i] in history:
                return [history[nums[i]], i]
            else:
                history[target - nums[i]] = i
