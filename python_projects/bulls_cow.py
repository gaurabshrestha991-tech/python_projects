from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        remaining_secret = []
        remaining_guess = []
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                remaining_secret.append(s)
                remaining_guess.append(g)
                
        secret_count = Counter(remaining_secret)
        guess_count = Counter(remaining_guess)
        
        cows = sum(
            min(secret_count[digit], guess_count[digit])
            for digit in secret_count
        )
        
        return f"{bulls}A{cows}B"
    
secret = "1807"
guess = "7810"

solution = Solution()
print(solution.getHint(secret, guess))
