# def compress(s):
#     counter = {}
#     res = ""

#     for i in range(len(s)):
#         char = s[i]
#         if i == 0:
#             counter[char] = 1
#             continue

#         if s[i] == s[i - 1]:
#             counter[char] += 1
#         else:
#             res += f"{s[i - 1]}{counter[s[i - 1]]}"
#             del counter[s[i - 1]]
#             counter[char] = 1

#     for key, val in counter.items():
#         res += f"{key}{val}"

#     return res

# optimization made is that we do not need a hash map
# O(N + (K^2)) 
# -> N is string length
# -> k is res string length (because of appending string) 

# K^2 can be reduced to linear if a sting builder is used

def compress(s):
    counter = 0
    res = ""

    for i in range(len(s)):
        counter += 1

        if (i + 1 == len(s)) or (s[i] != s[i + 1]):
            res += s[i]
            res += str(counter)
            counter = 0

    return s if len(res) == len(s) else res


print(compress("aabcccccaaa") == "a2b1c5a3")
print(compress("aabccc") == "aabccc")
print(compress("a") == "a1")
print(compress("abcdefghi") == "a1b1c1d1e1f1g1h1i1")
