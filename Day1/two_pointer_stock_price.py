def max_profit_two_pointers(prices):
    left=0
    right=1
    max_profit=0
    while right < len(prices):
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
        else:
            left = right
        right+=1
    return max_profit

def main():
    prices1 = [5,6,7,8,9,10]
    print(f"Prices: {prices1}, Max Profit: {max_profit_two_pointers(prices1)}")
    prices2 = [5,6,8,9,10]
    print(f"Prices: {prices2}, Max Profit: {max_profit_two_pointers(prices2)}")
    prices3 = [6,10,11]
    print(f"Prices: {prices3}, Max Profit: {max_profit_two_pointers(prices3)}")
    prices4 = [6,10,11,2,5,11,8,3,6]
    print(f"Prices: {prices4}, Max Profit: {max_profit_two_pointers(prices4)}")

if __name__ == "__main__":
    main()

