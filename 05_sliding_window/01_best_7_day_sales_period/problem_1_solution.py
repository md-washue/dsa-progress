def slide_window(list,w):
    i=0
    new_array=[]

    while(i<=(len(list)-w)):
        current= sum(list[i:i+w])
        new_array.append(current)

        i +=1



    return new_array




    ...


list= [3,8,2,5,7,6,12]
w=4
print(slide_window(list,w))


