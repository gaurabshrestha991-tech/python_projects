from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        
        sorted_indices = sorted(range(n), key=lambda i: score[i], reverse=True)
        
        result = [""] * n
        
        for rank, index in enumerate(sorted_indices):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)
                
        return result
    
if __name__ == "__main__":
    score = [10, 3, 8, 9, 4]
    
    obj = Solution()
    print(obj.findRelativeRanks(score))