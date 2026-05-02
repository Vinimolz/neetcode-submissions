class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        indices = []

        for i in range(len(nums)):
            wanted = target - nums[i]

            if wanted in memo:
                return [memo[wanted], i]

            memo[nums[i]] = i