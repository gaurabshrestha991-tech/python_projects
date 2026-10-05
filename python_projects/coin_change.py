def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    
    dp[0] = 0
    
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
                
    if dp[amount] == float('inf'):
        return -1
    
    return dp[amount]

def main():
    coins = [1,2,5]
    amount = 11
    
    result = coin_change(coins, amount)
    
    print("Coins: ", coins)
    print("Amount: ", amount)
    print("Minimum coins: ", result)
    
if __name__ == "__main__":
    main()
