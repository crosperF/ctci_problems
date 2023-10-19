
# O(N log N + N) => O(N log N)
# O(1)
def is_unique(s):
    if len(s) <= 1:
        return True

    arr = list(s)
    arr.sort()
    s = "".join(arr)

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


print(is_unique("crosper"))
print(is_unique("abcdefgh"))
print(is_unique("abcaefgh"))
