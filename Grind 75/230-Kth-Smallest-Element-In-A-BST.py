class Solution:
    def rob(self, nums) -> int:
        dp = [(0, 0) for i in range(len(nums) + 2)]
        current = len(nums) - 1
        while current >= 0:
            # Don't choose current house
            no = max(dp[current + 1])
            # Choose current house
            yes = nums[current] + max(dp[current + 2])
            dp[current] = (no, yes)
            current -= 1
        return max(dp[0])            
        
        
