# **Two Sum as a shopping problem**.
#  ### Real-life Two Sum problem
#  You’re at a grocery store with **RM50** to spend on exactly two items.
#  The prices are:
# ```
# [RM12, RM25, RM38, RM20, RM30]
# ```
#  You want to find **two different items whose prices add up to exactly RM50**.
#  For example:
# ```
# RM20 + RM30 = RM50
# ```
#  So the answer is the **two items priced RM20 and RM30**.
#  ### Your programming version
#  Imagine the store gives you:
# ```
# prices = [12, 25, 38, 20, 30]
# budget = 50
# ```
#  Your job is to find the **positions (indices)** of the two items whose prices add up to `50`.
#  Don't think about HashMaps yet.
#  **Question:** If you were standing in the store, how would you manually find the two items?

# ## The expected result is: [3, 4]

items=[12,25,38,20,30]
print(items)
# print(len(items))
for j in range (len(items)):
    for x in range (j+1, len(items)):
        the_sum=items[j]+items[x]
        if (the_sum == 50):
                    print("this is what we need",(j,x))

        #use these two lines for better understanding what is happening 
        # print(j,"|",x,"|",items[j],"|",items[x],"|", the_sum ) 
        # print("---------------------") 
        


