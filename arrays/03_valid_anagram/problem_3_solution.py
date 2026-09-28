# ///////practice////////
# import string 
# name= "Aka@@ aKa@@"
# # input_2= input("Ener the second input")
# print(name)
# print(name[::-1])

# if (name == (name[::-1])):
#     print(True)
# else:
#     print(False)


# if " " in name:
#     name=name.replace(" " , "")

# print(name)
# print(name[::-1])

# name =name.lower()
# print(name)
# print(name[::-1])

# if (name == (name[::-1])):
#     print(True)
# else:
#     print(False)


# for p in string.punctuation:
#     name=name.replace(p ,"")

# print(name)
# /////real_wrod/////////////


import string
def find_anagram (message_1,message_2):
    # removing uppercase
    message_1=message_1.lower()
    message_2= message_2.lower()

    #removing space
    message_1=message_1.replace(" " , "")
    message_2=message_2.replace(" ", "")

    for p in string.punctuation:
        message_1=message_1.replace(p, "")
        message_2=message_2.replace(p, "")



    message_1=sorted(message_1)
    message_2=sorted(message_2)

    print(f"This is the final message_1 {message_1}")
    print(f"This is the final message_2 {message_2}")

    return(message_1 == message_2)

 
message_1=str(input("Enter the first Message  "))
message_2=str(input("Enter the second Message  "))



print(find_anagram(message_1,message_2))