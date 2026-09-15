class Solution:
    def containsDuplicates(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False

nums = [1, 2, 3, 1]
solution = Solution()
result = solution.containsDuplicates(nums)

print(result)