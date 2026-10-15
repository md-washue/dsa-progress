def finding_duplicate(logins,k):
    i=0
    
    for i in range (len(logins)):
        window=logins[i:i+k]
        new_array=[]
        for j in window:
            if j in new_array:
                return True
                # new_array.append(j)
            else:
                new_array.append(j)

    return False
            


    
    ...




logins = ["amy", "bob", "carl", "bob", "dina"]
k = 4
print(finding_duplicate(logins,k))