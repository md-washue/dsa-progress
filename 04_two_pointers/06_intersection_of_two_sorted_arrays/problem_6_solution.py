def common_customers(team_a, team_b):
    i=0
    j=0
    common_IDs=[]
    while(i<len(team_a) and (j<len(team_b))):
        if team_a [i] == team_b[j]:
            value= team_a[i]
            if value not in common_IDs:
                common_IDs.append(value)

            i +=1
            j+=1
        elif(team_a[i]<team_b[j]):
            i +=1
        else:
            j +=1


    return(common_IDs)


    ...


team_a = [1, 2, 2, 3, 5, 8]
team_b = [2, 2, 3, 4, 8, 8]
print(common_customers(team_a,team_b))