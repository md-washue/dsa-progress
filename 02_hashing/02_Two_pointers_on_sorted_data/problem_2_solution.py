def two_sum_sorted(prices, target):

    for i in range (len(prices)):
        # print(i)
        for j in range(i,len(prices)):
            # print(j)
            if (prices[i]+prices[j] == target):
                print (i,j)


prices = [5, 10, 15, 20, 25, 30]
target=35
two_sum_sorted(prices,target)