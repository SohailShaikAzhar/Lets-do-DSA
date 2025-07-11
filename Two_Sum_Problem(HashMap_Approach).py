class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in val:
                return [val[difference], i]
            val[nums[i]] = i
