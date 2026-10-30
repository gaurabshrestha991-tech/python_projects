class Solution:
    def isPowerThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n % 3 == 0:
            n //= 3
            
        return n == 1
    
n = 27

solution = Solution()
print(solution.isPowerThree(n))
