# import punctuation 
import string
def is_palindrome(s):
    s=s.lower()
    for i in s:
        s=s.replace(" ", "")

    for p in string.punctuation:
        s=s.replace(p,"")

    print(s[::-1])
    if(s == s[::-1]):
        return True
    else:
        return False
    


s= "A man, a plan, a canal:Panama"
print(is_palindrome(s))