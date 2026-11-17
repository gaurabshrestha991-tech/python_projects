class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        positive_diag = set()
        negative_diag = set()
        
        count = 0
        
        def backtrack(row):
            nonlocal count
            
            if row == n:
                count += 1
                return 
            
            for col in range(n):
                
                if col in cols:
                    continue
                
                if (row + col) in positive_diag:
                    continue
                
                if (row - col) in negative_diag:
                    continue
                
                cols.add(col)
                positive_diag.add(row + col)
                negative_diag.add(row - col)
                
                backtrack(row + 1)
                
                cols.remove(col)
                positive_diag.remove(row + col)
                negative_diag.remove(row - col)
                
        backtrack(0)
        
        return count
