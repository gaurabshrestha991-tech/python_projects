class Solution:
    def ispalindrome(self, x):
        original = x
        reverse = 0
        
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
            
        return original == reverse
    
x = 121

solution = Solution()
result = solution.ispalindrome(x)

print(result)