from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == target:
                    return total
                
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        return closest
    
if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    
    solution = Solution()
    answer = solution.threeSumClosest(nums, target)
    
    print("Input:", nums)
    print("Target:", target)
    print("Output:", answer)
