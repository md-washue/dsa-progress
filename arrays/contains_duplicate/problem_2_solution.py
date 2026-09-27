# 🌍 Real-life scenario: Event check-in
# Imagine you're organizing a conference.
# Every person who enters the building scans their unique registration ID:
# A102
# B305
# C201
# A102
# D410
# Each registration ID is supposed to belong to one person.
# You need to detect whether the same ID was scanned more than once.
# For example:
# A102
# B305
# C201
# A102
# D410
# A102 appears twice.
# So the answer is:
# True
# because a duplicate exists.
# But:
# A102
# B305
# C201
# D410
# has no repeated ID:
# False

#answer

ID_list=["A102","B305","C201","A102","D410"]

found = False
for x in range(len(ID_list)):
    for i in range(x+1, len(ID_list)):
        if (ID_list[x] == ID_list[i]):
            found = True
            break

print(found)




            




