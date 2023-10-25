def palindrome_permutation(s):
    odd_count = 0
    counter = {}

    for c in s:
        if c == " ":
            continue
        c = c.lower()
        counter[c] = counter.get(c, 0) + 1

    for val in counter.values():
        if val % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True


def palindrome_permutation_2(s):
    counter = {}

    for c in s:
        if c == " ":
            continue
        c = c.lower()

        counter[c] = counter.get(c, 0) + 1
        if counter[c] == 2:
            del counter[c]

    return True if len(counter) <= 1 else False


# print(palindrome_permutation_2("kAm ak"))
# print(palindrome_permutation_2("ka mall"))
