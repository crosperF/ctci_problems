def rotate(mat):
    l, r = 0, len(mat) - 1
    t, b = 0, len(mat) - 1

    while l < r:
        for i in range(r - l):
            temp = mat[t][l + i]
            mat[t][l + i] = mat[b-i][l]
            mat[b-i][l] = mat[b][r - i]
            mat[b][r-i] = mat[t + i][r]
            mat[t + i][r] = temp

        l += 1
        t += 1
        r -= 1
        b -= 1


# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

# rotate(matrix)
# print(matrix)
