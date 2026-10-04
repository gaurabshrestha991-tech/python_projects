def canJump(nums):
    farthest = 0
    
    for i in range(len(nums)):
        if i > farthest:
            return False
        
        farthest = max(farthest, i + nums[i])
        
        if farthest >= len(nums) - 1:
            return True
        
    return True

nums = list(map(int, input("Enter numbers: ").split()))

answer = canJump(nums)
print(answer)
