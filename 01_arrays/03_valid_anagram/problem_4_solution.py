# ////practice
# def same_inventory(system_a, system_b):
    

    # for x in system_a:
    #     for y in system_b:
    #         # print(x,y)
    #         if(x == y):
    #             print("Here is a similor")
    #             print(similor_conuter)

    #             similor_conuter +=1
    #             print(similor_conuter)
    #             print(x,y)

    # print(similor_conuter)

    # if (similor_conuter == len(system_a)):
    #     print("both are same inventory")

# //answer

def same_inventory(system_a, system_b):

    count_a={}
    count_b={}

    for item in system_a:
        if item not in count_a:
            count_a[item] =1
        else:
            count_a[item] +=1

    for item in system_b:
        if item not in count_b:
            count_b[item] =1
        else:
            count_b[item] +=1

    print(count_a)
    print(count_b)

    return (count_a == count_b)




    




system_a= [
    "SKU-101",
    "SKU-205",
    "SKU-101",
    "SKU-300",
    "SKU-205"
]

system_b= [
    "SKU-205",
    "SKU-101",
    "SKU-205",
    "SKU-300",
    "SKU-101"
]

print(same_inventory(system_a,system_b))