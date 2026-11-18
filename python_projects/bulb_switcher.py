import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.isqrt(n)

if __name__ == "__main__":
    n = int(input("Enter the number of bulbs: "))

    solution = Solution()
    result = solution.bulbSwitch(n)

    print("Number of bulbs that remain ON:", result)
