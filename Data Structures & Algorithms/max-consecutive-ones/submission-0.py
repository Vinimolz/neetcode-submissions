class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        max_ones = 0
        for num in nums:
            if num == 1:
                ones += 1
            else:
                if ones > max_ones:
                    max_ones = ones
                ones = 0
                
        if ones > max_ones:
            return ones
        else:
            return max_ones