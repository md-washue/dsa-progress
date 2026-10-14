
def max_sales(sales,k):
    new_list=[]
    outputs=[]
   
    i=0
    while(i<=(len(sales)-k)):
        combining=sum(sales[i:i+k])
        outputs.append(combining)
        # print(combining)
        maximum= max(outputs)
        # print(maximum)
       
        if combining>=maximum:
            new_list.clear()
            perfect=sales[i:i+k]
            new_list.append(perfect)



        i+=1


    return (maximum,new_list)

    ...

sales =[120,200,150,300,250,100,180,400]
print(f"the list size is  {len(sales)}")
k=3

print(max_sales(sales,k))