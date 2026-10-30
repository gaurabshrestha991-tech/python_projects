class Solution:
    def readBinaryWatch(self, trunedOn: int) -> list[str]:
        result = []
        
        for hour in range(12):
            for minute in range(60):
                if (hour.bit_count() + minute.bit_count()) == turnedOn:
                    result.append(f"{hour}:{minute:02}")
                    
        return result
    
    
turnedOn = 1

solution = Solution()
result = solution.readBinaryWatch(turnedOn)

print(result)
