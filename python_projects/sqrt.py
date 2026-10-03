class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        i = 1
        
        while i * i <= x:
            i += 1
            
        return i - 1
    
    
x = int(input("Enter a number: "))

solution = Solution()
result = solution.mySqrt(x)

print("Integer square root: ", result)