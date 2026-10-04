def generateParenthesis(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
            
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
            
    backtrack("", 0, 0)
    
    return result
n = int(input("Enter n: "))

answer = generateParenthesis(n)
print("Valid combinations: ")

for combinations in answer:
    print(combinations)
