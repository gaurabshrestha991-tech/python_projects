class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0
        
        for money in nums:
            current = max(prev1, prev2 + money)
            
            prev2 = prev1
            prev1 = current
            
        return prev1
    
nums = [2, 7, 9, 3, 1]

solution = Solution()
result = solution.rob(nums)

print(result)
