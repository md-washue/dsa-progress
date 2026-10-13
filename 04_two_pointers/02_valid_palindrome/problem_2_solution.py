import string 
def is_palindrome(text):
    
    text=text.lower()
    text= text.replace(" " , "")
    # print(text)
    for i in string.punctuation:
        text= text.replace(i, "")
    # print(text)
    left=0
    right=len(text)-1

    while(left <= right):
        if (text[left] != text[right]):
            return False
        else:
            left +=1
            right -=1


    return True

    ...

text = "A man, a plan, a canal: Panama"
# text = "madam"
# text="Hello"
print(is_palindrome(text))
