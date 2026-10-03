class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        first =1 
        second = 2
        
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
            
        return second
    
n = int(input("Enter number of stairs: "))

solution = Solution()
result = solution.climbStairs(n)

print("Numbers of ways: ", result)