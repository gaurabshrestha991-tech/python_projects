pick = 6

def guess(num:int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            result = guess(mid)
            
            if result == 0:
                return mid
            
            elif result == -1:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return -1
    
solution = Solution()
print(solution.guessNumber(10))
