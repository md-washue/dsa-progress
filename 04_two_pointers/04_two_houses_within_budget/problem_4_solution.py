def best_house_pair(prices, budget):
    left=0
    right=len(prices)-1
    while(left<=right):
        total = prices[left] + prices[right]

        if (total == budget):
            return(prices[left],prices[right])
        elif(total<budget):
            left +=1
        else:
            right -=1
            # print(33)
    return None
    ...
prices = [100, 200, 300, 400, 500]
budget = 700
print(best_house_pair(prices,budget))
