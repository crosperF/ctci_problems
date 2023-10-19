# time: O(A + B) => O(A)
# space: O(A)

def check_perm(a, b):
    if len(a) != len(b):
        return False

    counter = {}

    for c in a:
        counter[c] = counter.get(c, 0) + 1

    for c in b:
        if (c not in counter or counter[c] <= 0):
            return False

    return True


print(check_perm("abcde", "decab"))
print(check_perm("abcde", "degab"))
