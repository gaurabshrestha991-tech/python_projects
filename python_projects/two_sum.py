nums = [2,7,11,15]
target = 26

def two_Sum(nums, target):
    seen = {}
    
    for i , num in enumerate(nums):
        needed = target - num
        
        if needed in seen:
            return[seen[needed], i]
        
        seen[num] = i
        
    return []
        
result = two_Sum(nums, target)

print("Indices: ", result)