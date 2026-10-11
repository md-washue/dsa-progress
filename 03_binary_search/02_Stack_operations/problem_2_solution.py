def browser_back(history):


    if len(history) == 0:
        return None
    else:
        return history.pop()

history=[
    "google.com",
    "youtube.com",
    "github.com"
]
print (history)

print(browser_back(history) )
print (history)
