def three_sum(nums):
    for i in range(len(nums)):
        for j in range(i+1, (len(nums))):
            for k in range(j+1, (len(nums))):
                if ((nums[i]+nums[j]+nums[k])== 0):
                    print(nums[i],nums[j],nums[k])



numsrices = [-4, -1, -1, 0, 1, 2]

three_sum(numsrices)

