def one_pass(a, b):
    if abs(len(a) - len(b)) >= 2:
        return False
    diff = 0

    if len(a) != len(b):
        diff += 1

    ctr1 = {}
    ctr2 = {}

    for c in a:
        ctr1[c] = ctr1.get(c, 0) + 1

    for c in b:
        ctr2[c] = ctr2.get(c, 0) + 1

    for key, val in ctr2.items():
        if key not in ctr1 or ctr1[key] != val:
            diff += 1

        if diff >= 2:
            return False

    return True

print(one_pass("pale", "ple"))
print(one_pass("pales", "pale"))
print(one_pass("pale", "bale"))
print(one_pass("pale", "bake"))
