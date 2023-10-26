
# O(m * n) - time
# O(m + n) - space

# def zero(mat):
#     rows = set()
#     cols = set()

#     for r in range(len(mat)):
#         for c in range(len(mat[0])):
#             if mat[r][c] == 0:
#                 rows.add(r)
#                 cols.add(c)

#     for r in range(len(mat)):
#         for c in range(len(mat[0])):
#             if (r in rows or
#                     c in cols):
#                 mat[r][c] = 0

# time - O(N)
# space - O(1)

def zero(mat):
    row_has_zero = False
    col_has_zero = False

    # check for first row zeros
    for r in range(len(mat)):
        if mat[r][0] == 0:
            row_has_zero = True
            break

    # check for first col zeros
    for c in range(len(mat[0])):
        if mat[0][c] == 0:
            col_has_zero = True
            break

    # set rows and cols to zero in the oth row and col
    for r in range(1, len(mat)):
        for c in range(1, len(mat[0])):
            if mat[r][c] == 0:
                mat[r][0] = 0
                mat[0][c] = 0

    # set cells to zero if the 0th index is zero
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][0] == 0 or mat[0][c] == 0:
                mat[r][c] = 0

    # set values for 0th index
    if row_has_zero:
        for r in range(len(mat)):
            mat[r][0] = 0

    if col_has_zero:
        for c in range(len(mat[0])):
            mat[0][c] = 0


matrix = [[1, 2, 3, 0],
          [5, 6, 7, 8],
          [9, 0, 11, 12],
          [13, 14, 15, 16]]

zero(matrix)
print(matrix)
