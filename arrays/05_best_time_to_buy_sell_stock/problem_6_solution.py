def max_profit(prices):
    min_price = prices[0]
    best_profit = 0

    for price in prices:

        profit = price - min_price

        if profit > best_profit:
            best_profit = profit

        if price < min_price:
            min_price = price

    return best_profit


prices = [120, 95, 80, 110, 150, 130, 170]

print(max_profit(prices))



for x in range (len(prices)):
    print(f"Day {x} RM{prices[x]}")
