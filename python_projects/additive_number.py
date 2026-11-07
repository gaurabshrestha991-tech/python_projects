class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        n = len(num)
        
        def backtrack(index, first, second, count):
            
            if index == n:
                return count >= 3
            
            for i in range(index, n):
                current = num[index:i + 1]
                
                if len(current) > 1 and current[0] == '0':
                    break
                third = str(int(first) + int(second)) if count >= 2 else current
                
                if count < 2 or current == third:
                    
                    if backtrack(i + 1,
                                 second if count >= 1 else current,
                                 current,
                                 count + 1):
                        return True
                    
            return False
        for i in range(1, n):
            
            first = num[:i]
            
            if len(first) > 1 and first[0] == '0':
                break
            
            for j in range(i + 1, n):
                second = num[i:j]
                
                if len(second) > 1 and second[0] == '0':
                    break
            
                if backtrack(j, first, second, 2):
                    return True
                
        return False
                    
