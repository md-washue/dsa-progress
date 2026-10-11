def daily_temperatures(temperatures):
    warmer_days=[]
    # print(temperatures)

    for i in range (len(temperatures)):
       
    #    if i==len(temperatures):
    #        warmer_days.append(0)
        
       for j in range (i+1 , len (temperatures)) :
        #    print(f"the date is {temperatures[i]}")
        #    print(f"the next date is {temperatures[j]}")
           if (temperatures[i]<temperatures[j]):
               diffence=(j-i)
            #    print(diffence)
               warmer_days.append(diffence)
               break
    else:
        warmer_days.append(0)    

    return warmer_days
    



temperatures = [30, 32, 31, 35, 34, 36]

print(daily_temperatures(temperatures))