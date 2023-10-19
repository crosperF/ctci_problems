# def urify(s, l):
#     res = ""
#     for i in range(l):
#         c = s[i]
#         if c == " ":
#             res += "%20"
#         else:
#             res += c

#     return res

# changing inplace
def urify(s, l):
    s = list(s)
    spaces = 0

    for i in range(l):
        if s[i] == " ":
            spaces += 1

    last_ptr = l + (spaces * 2) - 1

    for i in range(l - 1, -1, -1):
        if s[i] == " ":
            s[last_ptr] = "0"
            s[last_ptr - 1] = "2"
            s[last_ptr - 2] = "%"
            last_ptr -= 3
        else:
            s[last_ptr] = s[i]
            last_ptr -= 1

    s = "".join(s)
    return s


print(urify("mr john smith    ", 13))
