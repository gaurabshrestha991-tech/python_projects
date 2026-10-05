def num_islands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    islands = 0
    
    def dfs(row, col):
        
        if row < 0 or row >= rows:
            return 
        if col < 0 or col >= cols:
            return 
        
        if grid[row][col] == "0":
            return 
        
        grid[row][col] = "0"
        
        dfs(row - 1, col)
        
        dfs(row + 1, col)
        
        dfs(row, col - 1)
        
        dfs(row, col + 1)
        
    for row in range(rows):
        for col in range(cols):
            
            if grid[row][col] == "1":
                islands += 1
                dfs(row, col)
                
    return islands

def main():
    
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    result = num_islands(grid)
    
    print("Number of islands: ", result)
    
if __name__ == "__main__":
    main()
