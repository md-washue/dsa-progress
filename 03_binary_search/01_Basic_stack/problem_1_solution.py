# def is_valid(s):
#     output=True
#     for item in s:
#         if item =="[":
#             if "]" in (s[s.index(item)+1:]):
#                 pass
#             else:
#                 output=False
#         elif item == "{":
#             if "}" in (s[s.index(item)+1 :]):
#                 pass
#             else:
#                 output=False

#         elif item =="(":
#             if ")" in (s[s.index(item) +1:]):
#                 pass
#             else:
#                 output=False


def is_valid(s):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for item in s:
        if item in "([{":
            stack.append(item)

        else:
            if not stack:
                return False

            if stack.pop() != pairs[item]:
                return False

    return len(stack) == 0


s = "{[()]}"

print(is_valid(s))